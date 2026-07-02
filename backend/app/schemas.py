from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class Student(BaseModel):
    id: str
    name: str
    dept: str
    gender: str
    cgpa: float
    tenth: float
    twelfth: float
    aptitude: int
    communication: int
    technical: int
    coding: int
    projects: int
    internships: int
    certifications: int
    attendance: float
    backlogs: int
    status: str = "Not Placed"

class CompanyCriteria(BaseModel):
    name: str
    logo: str
    minCGPA: float
    minTenth: float
    minTwelfth: float
    maxBacklogs: int
    minCoding: int
    minAptitude: int
    minTechnical: int
    minCommunication: int
    minProjects: int
    minInternships: int
    minAttendance: float
    tier: str
    package: str
    color: str

class CriteriaComparisonItem(BaseModel):
    label: str
    required: str
    actual: str
    met: bool

class EvaluateRequest(BaseModel):
    student_id: str
    company_key: str

class EvaluateResponse(BaseModel):
    eligibility: str  # Eligible, Partially Eligible, Not Eligible
    readiness_score: int
    strengths: List[str]
    weaknesses: List[str]
    recommendations: List[str]
    reasoning: str
    criteria: List[CriteriaComparisonItem]
    company: CompanyCriteria

class PredictionResult(BaseModel):
    status: str
    probability: float

class ChatRequest(BaseModel):
    student_id: Optional[str] = None
    company_key: Optional[str] = None
    question: str

class ChatResponse(BaseModel):
    response: str
