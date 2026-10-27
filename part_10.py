
students = [
    {"name": "Aung Aung", "age": 21, "study_hours": 4.5, "score": 85},
    {"name": "Su Su", "age": 20, "study_hours": 3.0, "score": 65},
    {"name": "Mg Mg", "age": 22, "study_hours": 2.5, "score": 35},
    {"name": "Kyaw Kyaw", "age": 21, "study_hours": 5.0, "score": 90},
    {"name": "Zaw Zaw", "age": 20, "study_hours": 4.0, "score": 55}
]

grade_categories = ("Excellent", "Good", "Pass", "Fail")


def classify_grade(score):
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 80:
        return grade_categories[0]
    elif score >= 60:
        return grade_categories[1]
    elif score >= 40:
        return grade_categories[2]
    else:
        return grade_categories[3]


def calculate_average(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)


def count_passed(students):
    passed_count = 0
    for student in students:
        if 40 <= student["score"] <= 100:
            passed_count += 1
    return passed_count

print("===== STUDENT PERFORMANCE REPORT =====")

for student in students:
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Study Hours:", student["study_hours"])
    print("Score:", student["score"])
    print("Grade:", classify_grade(student["score"]))
    print()

# Summary Report
print("===== SUMMARY =====")

scores = [student["score"] for student in students]

total_students = len(students)
average_score = calculate_average(scores)
highest_score = max(scores)
lowest_score = min(scores)
passed_students = count_passed(students)
failed_students = total_students - passed_students
top_student = max(students, key=lambda student: student["score"])

print("Total Students:", total_students)
print("Average Score:", round(average_score, 2))
print("Highest Score:", highest_score)
print("Lowest Score:", lowest_score)
print("Passed Students:", passed_students)
print("Failed Students:", failed_students)
print("Top Student:", top_student["name"])
