def get_passed_students(students: dict, passing_score: int) -> dict:
    passed_students = {}
    for name, score in students.items():
        if score > passing_score:
            passed_students[name] = score
    
    return passed_students


students = {
    "Anna": 85,
    "John": 40,
    "Mike": 70
}
passed_students_list = get_passed_students(students, 60)
print(passed_students_list)