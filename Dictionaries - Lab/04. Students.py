elements = input()  ## students 4
students_ID = {}
students_course = {}

while True:
    if ':' not in elements:
        break
    elements = elements.split(':')
    students_ID[elements[0]] = elements[1]
    students_course[elements[0]] = elements[-1]
    elements = input()

for student, ID in students_ID.items():
    student_subject = students_course[student]
    if elements.startswith(student_subject):
        print(f'{student} - {ID}')
    elif student_subject == 'programming basics' and elements == 'programming_basics':
        print(f'{student} - {ID}')
