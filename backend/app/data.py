# ============================================================
# PlacementGPT — Student Database & Company Criteria (Python)
# ============================================================

STUDENTS = [
    {"id": "S001", "name": "Aarav Sharma", "dept": "CSE", "gender": "Male", "cgpa": 9.2, "tenth": 95.0, "twelfth": 92.0, "aptitude": 88, "communication": 82, "technical": 90, "coding": 92, "projects": 5, "internships": 2, "certifications": 4, "attendance": 94.0, "backlogs": 0, "status": "Placed"},
    {"id": "S002", "name": "Priya Patel", "dept": "CSE", "gender": "Female", "cgpa": 8.8, "tenth": 91.0, "twelfth": 89.0, "aptitude": 85, "communication": 88, "technical": 86, "coding": 88, "projects": 4, "internships": 2, "certifications": 3, "attendance": 92.0, "backlogs": 0, "status": "Placed"},
    {"id": "S003", "name": "Rahul Kumar", "dept": "CSE", "gender": "Male", "cgpa": 6.8, "tenth": 72.0, "twelfth": 68.0, "aptitude": 55, "communication": 48, "technical": 52, "coding": 58, "projects": 1, "internships": 0, "certifications": 1, "attendance": 78.0, "backlogs": 1, "status": "Not Placed"},
    {"id": "S004", "name": "Sneha Gupta", "dept": "CSE", "gender": "Female", "cgpa": 8.1, "tenth": 85.0, "twelfth": 82.0, "aptitude": 75, "communication": 72, "technical": 78, "coding": 76, "projects": 3, "internships": 1, "certifications": 3, "attendance": 90.0, "backlogs": 0, "status": "Placed"},
    {"id": "S005", "name": "Vikram Singh", "dept": "CSE", "gender": "Male", "cgpa": 5.9, "tenth": 62.0, "twelfth": 58.0, "aptitude": 42, "communication": 38, "technical": 40, "coding": 35, "projects": 0, "internships": 0, "certifications": 0, "attendance": 68.0, "backlogs": 3, "status": "Not Placed"},
    {"id": "S006", "name": "Ananya Reddy", "dept": "CSE", "gender": "Female", "cgpa": 9.0, "tenth": 93.0, "twelfth": 90.0, "aptitude": 90, "communication": 85, "technical": 88, "coding": 90, "projects": 6, "internships": 2, "certifications": 5, "attendance": 96.0, "backlogs": 0, "status": "Placed"},
    {"id": "S007", "name": "Arjun Nair", "dept": "CSE", "gender": "Male", "cgpa": 7.4, "tenth": 78.0, "twelfth": 75.0, "aptitude": 65, "communication": 60, "technical": 68, "coding": 70, "projects": 2, "internships": 1, "certifications": 2, "attendance": 85.0, "backlogs": 0, "status": "Placed"},
    {"id": "S008", "name": "Meera Joshi", "dept": "CSE", "gender": "Female", "cgpa": 9.5, "tenth": 97.0, "twelfth": 95.0, "aptitude": 92, "communication": 90, "technical": 94, "coding": 96, "projects": 7, "internships": 3, "certifications": 6, "attendance": 98.0, "backlogs": 0, "status": "Placed"},
    {"id": "S009", "name": "Karthik Iyer", "dept": "CSE", "gender": "Male", "cgpa": 6.2, "tenth": 65.0, "twelfth": 62.0, "aptitude": 45, "communication": 40, "technical": 48, "coding": 42, "projects": 1, "internships": 0, "certifications": 0, "attendance": 72.0, "backlogs": 2, "status": "Not Placed"},
    {"id": "S010", "name": "Divya Menon", "dept": "CSE", "gender": "Female", "cgpa": 7.6, "tenth": 80.0, "twelfth": 78.0, "aptitude": 68, "communication": 65, "technical": 70, "coding": 72, "projects": 2, "internships": 1, "certifications": 2, "attendance": 88.0, "backlogs": 0, "status": "Placed"},
    
    {"id": "S011", "name": "Rohan Desai", "dept": "IT", "gender": "Male", "cgpa": 8.0, "tenth": 83.0, "twelfth": 80.0, "aptitude": 72, "communication": 70, "technical": 75, "coding": 78, "projects": 3, "internships": 1, "certifications": 2, "attendance": 89.0, "backlogs": 0, "status": "Placed"},
    {"id": "S012", "name": "Kavitha Sundaram", "dept": "IT", "gender": "Female", "cgpa": 8.6, "tenth": 90.0, "twelfth": 87.0, "aptitude": 82, "communication": 80, "technical": 84, "coding": 85, "projects": 4, "internships": 2, "certifications": 3, "attendance": 93.0, "backlogs": 0, "status": "Placed"},
    {"id": "S013", "name": "Aditya Verma", "dept": "IT", "gender": "Male", "cgpa": 6.1, "tenth": 64.0, "twelfth": 60.0, "aptitude": 44, "communication": 42, "technical": 46, "coding": 40, "projects": 1, "internships": 0, "certifications": 0, "attendance": 70.0, "backlogs": 2, "status": "Not Placed"},
    {"id": "S014", "name": "Pooja Nambiar", "dept": "IT", "gender": "Female", "cgpa": 7.2, "tenth": 76.0, "twelfth": 74.0, "aptitude": 62, "communication": 58, "technical": 64, "coding": 66, "projects": 2, "internships": 1, "certifications": 1, "attendance": 84.0, "backlogs": 0, "status": "Placed"},
    {"id": "S015", "name": "Suresh Rajan", "dept": "IT", "gender": "Male", "cgpa": 5.5, "tenth": 58.0, "twelfth": 55.0, "aptitude": 35, "communication": 30, "technical": 38, "coding": 32, "projects": 0, "internships": 0, "certifications": 0, "attendance": 62.0, "backlogs": 4, "status": "Not Placed"},
    {"id": "S016", "name": "Lakshmi Krishnan", "dept": "IT", "gender": "Female", "cgpa": 7.8, "tenth": 82.0, "twelfth": 79.0, "aptitude": 70, "communication": 68, "technical": 72, "coding": 74, "projects": 3, "internships": 1, "certifications": 2, "attendance": 87.0, "backlogs": 0, "status": "Placed"},
    {"id": "S017", "name": "Nikhil Choudhary", "dept": "IT", "gender": "Male", "cgpa": 6.9, "tenth": 73.0, "twelfth": 70.0, "aptitude": 56, "communication": 50, "technical": 55, "coding": 52, "projects": 1, "internships": 0, "certifications": 1, "attendance": 76.0, "backlogs": 1, "status": "Not Placed"},
    {"id": "S018", "name": "Riya Das", "dept": "IT", "gender": "Female", "cgpa": 8.4, "tenth": 88.0, "twelfth": 85.0, "aptitude": 80, "communication": 78, "technical": 82, "coding": 84, "projects": 4, "internships": 2, "certifications": 3, "attendance": 91.0, "backlogs": 0, "status": "Placed"},
    {"id": "S019", "name": "Sanjay Pillai", "dept": "IT", "gender": "Male", "cgpa": 6.3, "tenth": 66.0, "twelfth": 63.0, "aptitude": 48, "communication": 44, "technical": 50, "coding": 46, "projects": 1, "internships": 0, "certifications": 0, "attendance": 74.0, "backlogs": 1, "status": "Not Placed"},
    {"id": "S020", "name": "Deepa Bhatt", "dept": "IT", "gender": "Female", "cgpa": 7.9, "tenth": 81.0, "twelfth": 78.0, "aptitude": 71, "communication": 69, "technical": 74, "coding": 75, "projects": 3, "internships": 1, "certifications": 2, "attendance": 88.0, "backlogs": 0, "status": "Placed"},
    
    {"id": "S021", "name": "Amit Tiwari", "dept": "ECE", "gender": "Male", "cgpa": 7.7, "tenth": 79.0, "twelfth": 77.0, "aptitude": 69, "communication": 64, "technical": 72, "coding": 68, "projects": 2, "internships": 1, "certifications": 2, "attendance": 86.0, "backlogs": 0, "status": "Placed"},
    {"id": "S022", "name": "Shreya Kapoor", "dept": "ECE", "gender": "Female", "cgpa": 8.5, "tenth": 89.0, "twelfth": 86.0, "aptitude": 81, "communication": 76, "technical": 83, "coding": 80, "projects": 4, "internships": 2, "certifications": 3, "attendance": 92.0, "backlogs": 0, "status": "Placed"},
    {"id": "S023", "name": "Rajesh Yadav", "dept": "ECE", "gender": "Male", "cgpa": 6.7, "tenth": 70.0, "twelfth": 67.0, "aptitude": 53, "communication": 48, "technical": 55, "coding": 50, "projects": 1, "internships": 0, "certifications": 1, "attendance": 77.0, "backlogs": 1, "status": "Not Placed"},
    {"id": "S024", "name": "Nisha Agarwal", "dept": "ECE", "gender": "Female", "cgpa": 6.0, "tenth": 63.0, "twelfth": 60.0, "aptitude": 43, "communication": 40, "technical": 45, "coding": 38, "projects": 0, "internships": 0, "certifications": 0, "attendance": 69.0, "backlogs": 2, "status": "Not Placed"},
    {"id": "S025", "name": "Varun Malhotra", "dept": "ECE", "gender": "Male", "cgpa": 7.1, "tenth": 75.0, "twelfth": 72.0, "aptitude": 60, "communication": 56, "technical": 62, "coding": 58, "projects": 2, "internships": 0, "certifications": 1, "attendance": 82.0, "backlogs": 0, "status": "Placed"},
    {"id": "S026", "name": "Swathi Prakash", "dept": "ECE", "gender": "Female", "cgpa": 7.9, "tenth": 82.0, "twelfth": 80.0, "aptitude": 73, "communication": 70, "technical": 75, "coding": 72, "projects": 3, "internships": 1, "certifications": 2, "attendance": 89.0, "backlogs": 0, "status": "Placed"},
    {"id": "S027", "name": "Manoj Dubey", "dept": "ECE", "gender": "Male", "cgpa": 5.6, "tenth": 59.0, "twelfth": 56.0, "aptitude": 36, "communication": 32, "technical": 38, "coding": 30, "projects": 0, "internships": 0, "certifications": 0, "attendance": 64.0, "backlogs": 3, "status": "Not Placed"},
    {"id": "S028", "name": "Gayathri Mohan", "dept": "ECE", "gender": "Female", "cgpa": 8.3, "tenth": 87.0, "twelfth": 84.0, "aptitude": 78, "communication": 75, "technical": 80, "coding": 82, "projects": 3, "internships": 1, "certifications": 3, "attendance": 91.0, "backlogs": 0, "status": "Placed"},
    
    {"id": "S029", "name": "Harish Saxena", "dept": "EEE", "gender": "Male", "cgpa": 7.0, "tenth": 74.0, "twelfth": 71.0, "aptitude": 58, "communication": 54, "technical": 60, "coding": 55, "projects": 2, "internships": 0, "certifications": 1, "attendance": 80.0, "backlogs": 0, "status": "Placed"},
    {"id": "S030", "name": "Priyanka Thakur", "dept": "EEE", "gender": "Female", "cgpa": 7.8, "tenth": 81.0, "twelfth": 78.0, "aptitude": 70, "communication": 67, "technical": 73, "coding": 70, "projects": 3, "internships": 1, "certifications": 2, "attendance": 87.0, "backlogs": 0, "status": "Placed"},
    {"id": "S031", "name": "Ganesh Babu", "dept": "EEE", "gender": "Male", "cgpa": 6.2, "tenth": 65.0, "twelfth": 61.0, "aptitude": 46, "communication": 42, "technical": 48, "coding": 44, "projects": 1, "internships": 0, "certifications": 0, "attendance": 73.0, "backlogs": 2, "status": "Not Placed"},
    {"id": "S032", "name": "Sunita Rao", "dept": "EEE", "gender": "Female", "cgpa": 6.8, "tenth": 71.0, "twelfth": 68.0, "aptitude": 54, "communication": 50, "technical": 56, "coding": 52, "projects": 1, "internships": 0, "certifications": 1, "attendance": 79.0, "backlogs": 1, "status": "Not Placed"},
    {"id": "S033", "name": "Kiran Mehta", "dept": "EEE", "gender": "Male", "cgpa": 7.6, "tenth": 80.0, "twelfth": 77.0, "aptitude": 67, "communication": 63, "technical": 70, "coding": 68, "projects": 2, "internships": 1, "certifications": 2, "attendance": 86.0, "backlogs": 0, "status": "Placed"},
    {"id": "S034", "name": "Anjali Pandey", "dept": "EEE", "gender": "Female", "cgpa": 8.7, "tenth": 90.0, "twelfth": 88.0, "aptitude": 84, "communication": 80, "technical": 85, "coding": 86, "projects": 4, "internships": 2, "certifications": 4, "attendance": 93.0, "backlogs": 0, "status": "Placed"},
    
    {"id": "S035", "name": "Ravi Shankar", "dept": "MECH", "gender": "Male", "cgpa": 6.6, "tenth": 69.0, "twelfth": 66.0, "aptitude": 52, "communication": 46, "technical": 54, "coding": 48, "projects": 1, "internships": 0, "certifications": 1, "attendance": 76.0, "backlogs": 1, "status": "Not Placed"},
    {"id": "S036", "name": "Neha Bose", "dept": "MECH", "gender": "Female", "cgpa": 7.5, "tenth": 79.0, "twelfth": 76.0, "aptitude": 66, "communication": 62, "technical": 68, "coding": 64, "projects": 2, "internships": 1, "certifications": 2, "attendance": 85.0, "backlogs": 0, "status": "Placed"},
    {"id": "S037", "name": "Prakash Hegde", "dept": "MECH", "gender": "Male", "cgpa": 5.8, "tenth": 61.0, "twelfth": 57.0, "aptitude": 40, "communication": 36, "technical": 42, "coding": 34, "projects": 0, "internships": 0, "certifications": 0, "attendance": 66.0, "backlogs": 3, "status": "Not Placed"},
    {"id": "S038", "name": "Tanvi Kulkarni", "dept": "MECH", "gender": "Female", "cgpa": 7.2, "tenth": 77.0, "twelfth": 73.0, "aptitude": 62, "communication": 58, "technical": 64, "coding": 60, "projects": 2, "internships": 0, "certifications": 1, "attendance": 83.0, "backlogs": 0, "status": "Placed"},
    {"id": "S039", "name": "Siddharth Ghosh", "dept": "MECH", "gender": "Male", "cgpa": 8.4, "tenth": 87.0, "twelfth": 85.0, "aptitude": 79, "communication": 74, "technical": 82, "coding": 80, "projects": 4, "internships": 2, "certifications": 3, "attendance": 92.0, "backlogs": 0, "status": "Placed"},
    {"id": "S040", "name": "Bhavana Shetty", "dept": "MECH", "gender": "Female", "cgpa": 6.0, "tenth": 63.0, "twelfth": 59.0, "aptitude": 43, "communication": 38, "technical": 44, "coding": 36, "projects": 0, "internships": 0, "certifications": 0, "attendance": 70.0, "backlogs": 2, "status": "Not Placed"},
    
    {"id": "S041", "name": "Arun Prasad", "dept": "CIVIL", "gender": "Male", "cgpa": 6.5, "tenth": 68.0, "twelfth": 65.0, "aptitude": 50, "communication": 46, "technical": 52, "coding": 45, "projects": 1, "internships": 0, "certifications": 1, "attendance": 75.0, "backlogs": 1, "status": "Not Placed"},
    {"id": "S042", "name": "Revathi Subramanian", "dept": "CIVIL", "gender": "Female", "cgpa": 7.7, "tenth": 80.0, "twelfth": 78.0, "aptitude": 69, "communication": 66, "technical": 71, "coding": 68, "projects": 3, "internships": 1, "certifications": 2, "attendance": 87.0, "backlogs": 0, "status": "Placed"},
    {"id": "S043", "name": "Dinesh Chauhan", "dept": "CIVIL", "gender": "Male", "cgpa": 5.7, "tenth": 60.0, "twelfth": 57.0, "aptitude": 38, "communication": 34, "technical": 40, "coding": 32, "projects": 0, "internships": 0, "certifications": 0, "attendance": 65.0, "backlogs": 3, "status": "Not Placed"},
    {"id": "S044", "name": "Madhavi Nair", "dept": "CIVIL", "gender": "Female", "cgpa": 6.9, "tenth": 72.0, "twelfth": 70.0, "aptitude": 56, "communication": 52, "technical": 58, "coding": 54, "projects": 1, "internships": 0, "certifications": 1, "attendance": 78.0, "backlogs": 1, "status": "Not Placed"},
    {"id": "S045", "name": "Vishnu Reddy", "dept": "CIVIL", "gender": "Male", "cgpa": 7.8, "tenth": 82.0, "twelfth": 79.0, "aptitude": 70, "communication": 65, "technical": 73, "coding": 70, "projects": 3, "internships": 1, "certifications": 2, "attendance": 88.0, "backlogs": 0, "status": "Placed"},
    
    {"id": "S046", "name": "Ishaan Chatterjee", "dept": "CSE", "gender": "Male", "cgpa": 9.4, "tenth": 96.0, "twelfth": 94.0, "aptitude": 91, "communication": 88, "technical": 93, "coding": 95, "projects": 6, "internships": 3, "certifications": 5, "attendance": 97.0, "backlogs": 0, "status": "Placed"},
    {"id": "S047", "name": "Fatima Sheikh", "dept": "CSE", "gender": "Female", "cgpa": 7.9, "tenth": 82.0, "twelfth": 79.0, "aptitude": 72, "communication": 70, "technical": 74, "coding": 76, "projects": 3, "internships": 1, "certifications": 2, "attendance": 89.0, "backlogs": 0, "status": "Placed"},
    {"id": "S048", "name": "Omkar Patil", "dept": "IT", "gender": "Male", "cgpa": 6.7, "tenth": 70.0, "twelfth": 67.0, "aptitude": 54, "communication": 48, "technical": 56, "coding": 52, "projects": 1, "internships": 0, "certifications": 1, "attendance": 77.0, "backlogs": 1, "status": "Not Placed"},
    {"id": "S049", "name": "Lavanya Murthy", "dept": "CSE", "gender": "Female", "cgpa": 8.2, "tenth": 86.0, "twelfth": 83.0, "aptitude": 76, "communication": 74, "technical": 79, "coding": 78, "projects": 3, "internships": 1, "certifications": 3, "attendance": 91.0, "backlogs": 0, "status": "Placed"},
    {"id": "S050", "name": "Dev Anand", "dept": "IT", "gender": "Male", "cgpa": 8.5, "tenth": 88.0, "twelfth": 86.0, "aptitude": 80, "communication": 76, "technical": 82, "coding": 84, "projects": 4, "internships": 2, "certifications": 3, "attendance": 92.0, "backlogs": 0, "status": "Placed"}
]

COMPANIES = {
    "TCS": {
        "name": "Tata Consultancy Services",
        "logo": "🏢",
        "minCGPA": 6.0, "minTenth": 60.0, "minTwelfth": 60.0, "maxBacklogs": 0,
        "minCoding": 50, "minAptitude": 50, "minTechnical": 0, "minCommunication": 0,
        "minProjects": 0, "minInternships": 0, "minAttendance": 75.0,
        "tier": "Mass Recruiter", "package": "3.6 - 7 LPA",
        "color": "#0072C6"
    },
    "Infosys": {
        "name": "Infosys Limited",
        "logo": "🏛️",
        "minCGPA": 6.5, "minTenth": 60.0, "minTwelfth": 60.0, "maxBacklogs": 0,
        "minCoding": 55, "minAptitude": 55, "minTechnical": 50, "minCommunication": 0,
        "minProjects": 0, "minInternships": 0, "minAttendance": 75.0,
        "tier": "Mass Recruiter", "package": "3.6 - 8 LPA",
        "color": "#007CC3"
    },
    "Wipro": {
        "name": "Wipro Limited",
        "logo": "🌐",
        "minCGPA": 6.0, "minTenth": 55.0, "minTwelfth": 55.0, "maxBacklogs": 0,
        "minCoding": 45, "minAptitude": 50, "minTechnical": 0, "minCommunication": 0,
        "minProjects": 0, "minInternships": 0, "minAttendance": 70.0,
        "tier": "Mass Recruiter", "package": "3.5 - 6.5 LPA",
        "color": "#44195B"
    },
    "Cognizant": {
        "name": "Cognizant Technology Solutions",
        "logo": "⚡",
        "minCGPA": 6.5, "minTenth": 60.0, "minTwelfth": 60.0, "maxBacklogs": 0,
        "minCoding": 50, "minAptitude": 55, "minTechnical": 50, "minCommunication": 0,
        "minProjects": 0, "minInternships": 0, "minAttendance": 75.0,
        "tier": "Mass Recruiter", "package": "4 - 8 LPA",
        "color": "#1A4788"
    },
    "Accenture": {
        "name": "Accenture",
        "logo": "💎",
        "minCGPA": 6.5, "minTenth": 65.0, "minTwelfth": 65.0, "maxBacklogs": 0,
        "minCoding": 55, "minAptitude": 60, "minTechnical": 55, "minCommunication": 50,
        "minProjects": 1, "minInternships": 0, "minAttendance": 75.0,
        "tier": "Premium Recruiter", "package": "4.5 - 11 LPA",
        "color": "#A100FF"
    },
    "Google": {
        "name": "Google",
        "logo": "🔍",
        "minCGPA": 8.0, "minTenth": 75.0, "minTwelfth": 75.0, "maxBacklogs": 0,
        "minCoding": 85, "minAptitude": 80, "minTechnical": 80, "minCommunication": 70,
        "minProjects": 3, "minInternships": 1, "minAttendance": 80.0,
        "tier": "Dream Company", "package": "30 - 50 LPA",
        "color": "#4285F4"
    },
    "Microsoft": {
        "name": "Microsoft",
        "logo": "🪟",
        "minCGPA": 7.5, "minTenth": 70.0, "minTwelfth": 70.0, "maxBacklogs": 0,
        "minCoding": 80, "minAptitude": 75, "minTechnical": 75, "minCommunication": 65,
        "minProjects": 2, "minInternships": 1, "minAttendance": 80.0,
        "tier": "Dream Company", "package": "25 - 45 LPA",
        "color": "#00A4EF"
    },
    "Amazon": {
        "name": "Amazon",
        "logo": "📦",
        "minCGPA": 7.0, "minTenth": 65.0, "minTwelfth": 65.0, "maxBacklogs": 0,
        "minCoding": 80, "minAptitude": 70, "minTechnical": 70, "minCommunication": 60,
        "minProjects": 2, "minInternships": 0, "minAttendance": 75.0,
        "tier": "Dream Company", "package": "20 - 40 LPA",
        "color": "#FF9900"
    }
}

def predict_placement(student: dict) -> dict:
    """
    Simulated placement prediction model using a weighted heuristic formula
    mimicking a machine learning classification model.
    """
    # Base logic: features contributing to placement probability
    # CGPA, Coding Score, Aptitude, Projects, Internships, Backlogs (Penalty)
    
    # Normalized features
    cgpa_norm = student.get("cgpa", 0.0) / 10.0
    coding_norm = student.get("coding", 0) / 100.0
    technical_norm = student.get("technical", 0) / 100.0
    aptitude_norm = student.get("aptitude", 0) / 100.0
    projects_norm = min(1.0, student.get("projects", 0) / 4.0)
    internships_norm = min(1.0, student.get("internships", 0) / 2.0)
    
    # Weighted contribution
    prob = (
        0.25 * cgpa_norm +
        0.20 * coding_norm +
        0.15 * technical_norm +
        0.15 * aptitude_norm +
        0.15 * projects_norm +
        0.10 * internships_norm
    )
    
    # Penalties
    if student.get("backlogs", 0) > 0:
        prob -= 0.15 * student.get("backlogs", 0)
    
    if student.get("attendance", 0.0) < 75.0:
        prob -= 0.10
        
    # Standardize probability between 0 and 1
    prob = max(0.0, min(1.0, prob))
    
    # Let's add slight determinism based on student ID to make it feel like a real ML prediction
    # which is consistent for the same student
    char_sum = sum(ord(c) for c in student.get("id", "S001"))
    offset = ((char_sum % 10) - 5) / 100.0  # -5% to +4% variability
    prob = max(0.1, min(0.98, prob + offset))
    
    status = "Placed" if prob >= 0.55 else "Not Placed"
    
    return {
        "status": status,
        "probability": round(prob, 4)
    }
