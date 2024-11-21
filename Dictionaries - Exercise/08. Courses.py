command = input()
students = {}

while command != 'end':
    course_name, student_name = command.split(" : ")

    if course_name not in students:
        students[course_name] = []
    students[course_name].append(student_name)

    command = input()

for course_name, student_list in students.items():
    print(f"{course_name}: {len(student_list)}")
    for student in student_list:
        print(f"-- {student}")
