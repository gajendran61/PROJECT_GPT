from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict, Any

# Local imports
from app.schemas import (
    Student, CompanyCriteria, EvaluateRequest, EvaluateResponse, 
    CriteriaComparisonItem, PredictionResult, ChatRequest, ChatResponse
)
from app.data import STUDENTS, COMPANIES, predict_placement
from app.database import get_retrieved_context, simulated_llama_agent_response

app = FastAPI(title="PlacementGPT API", version="1.0")

# Enable CORS for Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to PlacementGPT FastAPI Backend"}

@app.get("/api/students", response_model=List[Student])
def get_all_students():
    return STUDENTS

@app.get("/api/students/{student_id}", response_model=Student)
def get_student(student_id: str):
    for s in STUDENTS:
        if s["id"] == student_id:
            return s
    raise HTTPException(status_code=404, detail="Student not found")

@app.post("/api/students", response_model=Student)
def add_student(student: Student):
    # Insert at the beginning
    STUDENTS.insert(0, student.model_dump())
    return student

@app.get("/api/companies", response_model=Dict[str, CompanyCriteria])
def get_companies():
    return COMPANIES

@app.post("/api/evaluate", response_model=EvaluateResponse)
def evaluate_student(req: EvaluateRequest):
    student = next((s for s in STUDENTS if s["id"] == req.student_id), None)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
        
    company = COMPANIES.get(req.company_key)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")

    # Construct Criteria Comparison
    criteria_list = [
        CriteriaComparisonItem(label="CGPA", required=f">= {company['minCGPA']}", actual=str(student['cgpa']), met=student['cgpa'] >= company['minCGPA']),
        CriteriaComparisonItem(label="10th Percentage", required=f">= {company['minTenth']}%", actual=f"{student['tenth']}%", met=student['tenth'] >= company['minTenth']),
        CriteriaComparisonItem(label="12th Percentage", required=f">= {company['minTwelfth']}%", actual=f"{student['twelfth']}%", met=student['twelfth'] >= company['minTwelfth']),
        CriteriaComparisonItem(label="Active Backlogs", required=f"<= {company['maxBacklogs']}", actual=str(student['backlogs']), met=student['backlogs'] <= company['maxBacklogs'])
    ]
    if company['minCoding'] > 0: criteria_list.append(CriteriaComparisonItem(label="Coding Score", required=f">= {company['minCoding']}", actual=str(student['coding']), met=student['coding'] >= company['minCoding']))
    if company['minAptitude'] > 0: criteria_list.append(CriteriaComparisonItem(label="Aptitude Score", required=f">= {company['minAptitude']}", actual=str(student['aptitude']), met=student['aptitude'] >= company['minAptitude']))
    if company['minTechnical'] > 0: criteria_list.append(CriteriaComparisonItem(label="Technical Score", required=f">= {company['minTechnical']}", actual=str(student['technical']), met=student['technical'] >= company['minTechnical']))
    if company['minCommunication'] > 0: criteria_list.append(CriteriaComparisonItem(label="Communication Score", required=f">= {company['minCommunication']}", actual=str(student['communication']), met=student['communication'] >= company['minCommunication']))
    if company['minProjects'] > 0: criteria_list.append(CriteriaComparisonItem(label="Projects", required=f">= {company['minProjects']}", actual=str(student['projects']), met=student['projects'] >= company['minProjects']))
    if company['minInternships'] > 0: criteria_list.append(CriteriaComparisonItem(label="Internships", required=f">= {company['minInternships']}", actual=str(student['internships']), met=student['internships'] >= company['minInternships']))
    if company['minAttendance'] > 0: criteria_list.append(CriteriaComparisonItem(label="Attendance", required=f">= {company['minAttendance']}%", actual=f"{student['attendance']}%", met=student['attendance'] >= company['minAttendance']))

    met_count = sum(1 for c in criteria_list if c.met)
    total_criteria = len(criteria_list)
    
    if met_count == total_criteria: eligibility = "Eligible"
    elif met_count >= total_criteria * 0.7: eligibility = "Partially Eligible"
    else: eligibility = "Not Eligible"
    
    # Readiness score logic
    readiness_score = int(
        (student['cgpa']/10)*20 + (student['coding']/100)*18 + (student['technical']/100)*15 +
        (student['aptitude']/100)*12 + (student['communication']/100)*10 +
        min(1.0, student['projects']/4)*8 + min(1.0, student['internships']/2)*7 +
        min(1.0, student['certifications']/3)*5 + (student['attendance']/100)*5
    )
    if student['backlogs'] > 0: readiness_score -= (5 * student['backlogs'])
    readiness_score = max(0, min(100, readiness_score))

    # We will compute strengths and weaknesses via the database logic dynamically.
    from app.database import _generate_strengths, _generate_weaknesses, _generate_recommendations
    
    return EvaluateResponse(
        eligibility=eligibility,
        readiness_score=readiness_score,
        strengths=_generate_strengths(student),
        weaknesses=_generate_weaknesses(student),
        recommendations=_generate_recommendations(student),
        reasoning=f"Student met {met_count} out of {total_criteria} criteria for {company['name']}.",
        criteria=criteria_list,
        company=company
    )

@app.post("/api/chat", response_model=ChatResponse)
def chat_agent(req: ChatRequest):
    # Retrieve relevant context from ChromaDB based on the user's question
    context = get_retrieved_context(req.question)
    
    # Locate student if provided
    student_profile = {}
    if req.student_id:
        student_profile = next((s for s in STUDENTS if s["id"] == req.student_id), {})
        
    # Get ML Prediction
    prediction_result = {}
    if student_profile:
        prediction_result = predict_placement(student_profile)
        
    # Company data
    company_data = None
    if req.company_key:
        company_data = COMPANIES.get(req.company_key)
        
    # For a realistic evaluation data pass-in
    evaluation_data = None
    if student_profile and company_data:
        # Run a quick check
        from app.database import _generate_strengths
        # Use our deterministic heuristic from earlier
        readiness_score = int(
            (student_profile.get('cgpa',0)/10)*20 + (student_profile.get('coding',0)/100)*18 + 
            (student_profile.get('technical',0)/100)*15 + (student_profile.get('aptitude',0)/100)*12 + 
            (student_profile.get('communication',0)/100)*10 + 8 + 7 + 5 + 5
        )
        if student_profile.get('backlogs',0) > 0: readiness_score -= 5
        readiness_score = max(0, min(100, readiness_score))
        
        eligibility = "Eligible" if student_profile.get('cgpa',0) >= company_data['minCGPA'] and student_profile.get('backlogs',0) <= company_data['maxBacklogs'] else "Not Eligible"
        evaluation_data = {"eligibility": eligibility, "readiness_score": readiness_score}

    # Generate response
    response_text = simulated_llama_agent_response(
        context=context,
        student_profile=student_profile,
        prediction_result=prediction_result,
        question=req.question,
        company_data=company_data,
        evaluation_data=evaluation_data
    )
    
    return ChatResponse(response=response_text)
