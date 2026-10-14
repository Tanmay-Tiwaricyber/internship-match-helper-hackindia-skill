"""Reusable text-cleaning and internship matching logic."""
from mock_api import get_internships


def clean_text(value):
    """Normalize a string for case-insensitive skill comparisons."""
    return " ".join(str(value).strip().lower().split())


def normalize_skills(skills):
    """Return unique, non-empty normalized skills."""
    return sorted({clean_text(skill) for skill in skills if clean_text(skill)})


def score_internship(student_skills, internship):
    required = normalize_skills(internship.get("required_skills", []))
    student_set = set(student_skills)
    matched = [skill for skill in required if skill in student_set]
    missing = [skill for skill in required if skill not in student_set]
    score = round((len(matched) / len(required)) * 100) if required else 0
    return {
        "internship_id": internship.get("id", ""),
        "title": internship.get("title", "Untitled internship"),
        "company": internship.get("company", "Unknown company"),
        "location": internship.get("location", "Not specified"),
        "match_score": score,
        "matched_skills": matched,
        "missing_skills": missing,
    }


def build_matches(payload):
    """Build ranked internship matches from a JSON-compatible payload."""
    internships = get_internships(payload)
    students = payload.get("students", [])
    result_students = []

    for student in students:
        skills = normalize_skills(student.get("skills", []))
        ranked = [
            score_internship(skills, internship)
            for internship in internships
        ]
        ranked.sort(key=lambda item: (-item["match_score"], item["title"].lower()))
        result_students.append({
            "student_id": student.get("id", ""),
            "student_name": student.get("name", "Unknown student"),
            "skills": skills,
            "matches": ranked,
        })

    return {
        "project": "Internship Match Helper",
        "mode": "mock",
        "students": result_students,
    }
