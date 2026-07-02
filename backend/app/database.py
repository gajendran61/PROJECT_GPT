import chromadb
from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_community.embeddings import FakeEmbeddings
from typing import Dict, Any, List, Optional
import json

# Setup ChromaDB and a Mock Embedding (for simplicity and zero-dependency speed)
# In production, you would use HuggingFaceEmbeddings or similar.
embeddings = FakeEmbeddings(size=128)
chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name="placement_docs")

# Seed the Vector Database with Placement Policies and Company Rules
DOCUMENTS = [
    Document(page_content="Students with active backlogs are generally not eligible for premium and dream tier companies. Mass recruiters like TCS and Wipro strictly require 0 active backlogs.", metadata={"source": "placement_policy", "topic": "backlogs"}),
    Document(page_content="A minimum CGPA of 6.0 is the baseline for most placements. Premium companies require >= 6.5, and dream companies like Google and Microsoft require >= 7.5.", metadata={"source": "placement_policy", "topic": "cgpa"}),
    Document(page_content="High coding scores (>= 80) and practical project experience (>= 2 projects) significantly boost placement chances, especially for product-based roles.", metadata={"source": "career_advice", "topic": "skills"}),
    Document(page_content="Attendance below 75% disqualifies candidates from campus placement drives.", metadata={"source": "placement_policy", "topic": "attendance"}),
    Document(page_content="TCS requires 6.0 CGPA, 0 backlogs, and tests basic coding and aptitude. Infosys requires 6.5 CGPA and tests technical and aptitude skills.", metadata={"source": "company_rules", "topic": "mass_recruiters"}),
    Document(page_content="Google and Microsoft demand exceptional problem-solving skills, high CGPA (>= 7.5), and strong projects.", metadata={"source": "company_rules", "topic": "dream_companies"})
]

# Simple in-memory Chroma setup with LangChain wrapper
vectorstore = Chroma.from_documents(documents=DOCUMENTS, embedding=embeddings, collection_name="placement_docs", client=chroma_client)
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

def get_retrieved_context(query: str) -> str:
    """Retrieve relevant documents for the query."""
    docs = retriever.invoke(query)
    return "\n\n".join([d.page_content for d in docs])

def _generate_strengths(student: Dict[str, Any]) -> List[str]:
    s = []
    if student.get("cgpa", 0) >= 8.0: s.append(f"Excellent academic performance (CGPA: {student['cgpa']})")
    if student.get("coding", 0) >= 80: s.append(f"Strong coding proficiency ({student['coding']}/100)")
    if student.get("projects", 0) >= 3: s.append(f"Impressive project portfolio ({student['projects']} projects)")
    if student.get("internships", 0) >= 1: s.append("Valuable practical internship experience")
    if student.get("backlogs", 0) == 0: s.append("Clean academic record with 0 active backlogs")
    if not s: s.append("Currently enrolled and completing degree requirements")
    return s

def _generate_weaknesses(student: Dict[str, Any]) -> List[str]:
    w = []
    if student.get("cgpa", 0) < 6.5: w.append(f"Low CGPA ({student['cgpa']}) limits placement opportunities")
    if student.get("coding", 0) < 60: w.append("Coding skills need significant improvement")
    if student.get("communication", 0) < 60: w.append("Communication and soft skills need polishing")
    if student.get("backlogs", 0) > 0: w.append(f"Active backlogs ({student['backlogs']}) are a major blocker")
    if student.get("attendance", 0) < 75: w.append("Attendance is below the required 75% threshold")
    if not w: w.append("No major weaknesses identified")
    return w

def _generate_recommendations(student: Dict[str, Any]) -> List[str]:
    r = []
    if student.get("backlogs", 0) > 0: r.append("Clear active backlogs immediately to become eligible for drives.")
    if student.get("coding", 0) < 70: r.append("Practice DSA and competitive coding daily on platforms like LeetCode.")
    if student.get("communication", 0) < 70: r.append("Participate in mock interviews and group discussions to improve fluency.")
    if student.get("projects", 0) < 2: r.append("Build and deploy 1-2 full-stack or domain-specific projects to strengthen resume.")
    if not r: r.append("Maintain current performance and begin advanced interview preparation.")
    return r

def simulated_llama_agent_response(
    context: str,
    student_profile: Dict[str, Any],
    prediction_result: Dict[str, Any],
    question: str,
    company_data: Optional[Dict[str, Any]] = None,
    evaluation_data: Optional[Dict[str, Any]] = None
) -> str:
    """
    A deterministic simulator that precisely matches the required output template 
    for the PlacementGPT Master Agent Prompt, avoiding PyTorch/Transformers overhead.
    """
    
    # 1. Determine Eligibility and Readiness
    eligibility_status = "Not Eligible"
    readiness_score = 0
    if evaluation_data:
        eligibility_status = evaluation_data.get("eligibility", "Not Eligible")
        readiness_score = evaluation_data.get("readiness_score", 0)
    else:
        # Fallback heuristic
        if student_profile.get("backlogs", 0) > 0: eligibility_status = "Not Eligible"
        elif student_profile.get("cgpa", 0) >= 6.5: eligibility_status = "Eligible"
        else: eligibility_status = "Partially Eligible"
        
        # Simple score
        readiness_score = int((student_profile.get("cgpa", 0)/10)*30 + student_profile.get("coding", 0)*0.3 + student_profile.get("technical", 0)*0.2 + student_profile.get("aptitude", 0)*0.2)

    # 2. Extract strengths, weaknesses, recommendations
    strengths = _generate_strengths(student_profile)
    weaknesses = _generate_weaknesses(student_profile)
    recommendations = _generate_recommendations(student_profile)
    
    # 3. Formulate Reasoning
    reasoning = f"Based on the retrieved context, {student_profile.get('name')} has a readiness score of {readiness_score}/100. "
    if prediction_result:
        reasoning += f"The prediction model indicates a '{prediction_result.get('status')}' status with a {prediction_result.get('probability', 0)*100:.1f}% probability. "
    if company_data:
        reasoning += f"For {company_data.get('name', 'the company')}, the student is {eligibility_status}. "
    if student_profile.get("backlogs", 0) > 0:
        reasoning += "Active backlogs are a severe restriction according to campus policies. "
    elif student_profile.get("cgpa", 0) >= 8.0:
        reasoning += "A high CGPA combined with good technical skills makes this profile highly competitive. "
    reasoning += "The student should focus on the recommended areas to maximize placement success."

    # 4. Construct Final Text output according to Template
    response_lines = [
        "Eligibility Status:",
        eligibility_status,
        "",
        "Placement Readiness Score:",
        f"{readiness_score}/100",
        "",
        "Strengths:"
    ]
    for s in strengths: response_lines.append(f"• {s}")
    
    response_lines.extend(["", "Areas for Improvement:"])
    for w in weaknesses: response_lines.append(f"• {w}")
    
    response_lines.extend(["", "Recommendations:"])
    for r in recommendations: response_lines.append(f"• {r}")
    
    response_lines.extend(["", "Reasoning:", reasoning])
    
    return "\n".join(response_lines)
