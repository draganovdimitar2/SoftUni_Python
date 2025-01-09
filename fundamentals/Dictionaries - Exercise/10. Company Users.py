command = input()
db = {}
while command != 'End':
    company, employee_id = command.split(' -> ')

    if company not in db:
        db[company] = []
    if employee_id not in db[company]:
        db[company].append(employee_id)

    command = input()

for company, employee in db.items():
    print(f'{company}')
    for id in employee:
        print(f'-- {id}')
