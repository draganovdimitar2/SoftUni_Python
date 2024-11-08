def add_lesson(list_of_lessons, title):
    if title not in list_of_lessons:
        list_of_lessons.append(title)
    return list_of_lessons


def insert_lesson(list_of_lessons, title, index_of_inserting):
    if title not in list_of_lessons:
        list_of_lessons.insert(index_of_inserting, title)
    return list_of_lessons


def remove_lesson(list_of_lessons, title):
    if title in list_of_lessons:
        title_index = list_of_lessons.index(title)
        if title_index + 1 in range(len(list_of_lessons)):
            if "Exercise" in list_of_lessons[title_index + 1]:  # if list_of_lessons[title_index +1] == f"Exercise":
                list_of_lessons.pop(title_index + 1)
        list_of_lessons.remove(title)
    return list_of_lessons


def swap_lesson(list_of_lessons, first_lesson, second_lesson):
    if first_lesson in list_of_lessons and second_lesson in list_of_lessons:
        first_position = list_of_lessons.index(first_lesson)
        second_position = list_of_lessons.index(second_lesson)
        first_lesson_has_exercise = False
        second_lesson_has_exercise = False
        if first_position + 1 in range(len(list_of_lessons)):
            first_lesson_has_exercise = "Exercise" in list_of_lessons[first_position + 1]
        if second_position + 1 in range(len(list_of_lessons)):
            second_lesson_has_exercise = "Exercise" in list_of_lessons[second_position + 1]
        # Swap lessons
        list_of_lessons[first_position], list_of_lessons[second_position] = list_of_lessons[second_position], \
            list_of_lessons[first_position]
        # Swap exercises
        if first_lesson_has_exercise and second_lesson_has_exercise:
            list_of_lessons[first_position + 1], list_of_lessons[second_position + 1] = \
                list_of_lessons[second_position + 1], list_of_lessons[first_position + 1]
        elif not first_lesson_has_exercise and second_lesson_has_exercise:
            # list_of_lessons.insert(first_position + 1, list_of_lessons[second_position + 1])
            # list_of_lessons.pop(second_position + 1)
            list_of_lessons.insert(first_position + 1, list_of_lessons.pop(second_position + 1))
        elif first_lesson_has_exercise and not second_lesson_has_exercise:
            # list_of_lessons.insert(second_position +1, list_of_lessons[first_position + 1])
            # list_of_lessons.pop(first_position + 1)
            list_of_lessons.insert(second_position + 1, list_of_lessons.pop(first_position + 1))
    return list_of_lessons


def exercise(list_of_lessons, title):
    exercise_name = f"{title}-Exercise"
    if title in list_of_lessons and exercise_name not in list_of_lessons:
        lesson_index = list_of_lessons.index(title)
        list_of_lessons.insert(lesson_index + 1, exercise_name)
    elif title not in list_of_lessons:
        list_of_lessons.append(title)
        list_of_lessons.append(exercise_name)
    return list_of_lessons


lessons = input().split(", ")
command = input().split(":")
while len(command) > 1:
    action = command[0]
    lesson_title = command[1]
    if action == "Add":
        lessons = add_lesson(lessons, lesson_title)
    elif action == "Insert":
        index = int(command[2])
        lessons = insert_lesson(lessons, lesson_title, index)
    elif action == "Remove":
        lessons = remove_lesson(lessons, lesson_title)
    elif action == "Swap":
        next_lesson_title = command[2]
        lessons = swap_lesson(lessons, lesson_title, next_lesson_title)
    elif action == "Exercise":
        lessons = exercise(lessons, lesson_title)
    command = input().split(":")
for index, lesson_or_exercise in enumerate(lessons):
    print(f"{index + 1}.{lesson_or_exercise}")