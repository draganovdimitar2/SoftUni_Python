rows = int(input())
students = {}
for _ in range(rows):
    name = input()
    grade = float(input())

    if name not in students:
        students[name] = []
    students[name].append(grade)

students = {name: grades for name, grades in students.items() if
            sum(grades) / len(grades) >= 4.5}  # remove the students with avg grade under 4.5
for student_name, grade in students.items():
    average_grade = sum(grade) / len(grade)
    print(f"{student_name} -> {average_grade:.2f}")
