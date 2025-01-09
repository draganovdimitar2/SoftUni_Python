users_points_dictionary = {}
courses_dictionary = {}

while True:
    result = input().split("-")
    if len(result) == 1:  # exam finished received
        break
    elif len(result) == 2:  # User banned
        banned_name = result[0]
        del users_points_dictionary[banned_name]
    else:
        name, course, points = result[0], result[1], int(result[2])
        if name not in users_points_dictionary:
            users_points_dictionary[name] = 0
        if points > users_points_dictionary[name]:
            users_points_dictionary[name] = points
        if course not in courses_dictionary.keys():
            courses_dictionary[course] = 0
        courses_dictionary[course] += 1

print("Results:")
for name, points in users_points_dictionary.items():
    print(f"{name} | {points}")
print("Submissions:")
for language, submissions in courses_dictionary.items():
    print(f"{language} - {submissions}")
