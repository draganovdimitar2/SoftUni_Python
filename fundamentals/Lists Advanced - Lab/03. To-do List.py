to_do_list = []

while True:
    note = input()

    if note == "End":
        break

    importance, task = note.split('-')
    importance = int(importance)
    to_do_list.append((importance, task))

to_do_list.sort()
sorted_tasks = [task for _, task in to_do_list]
print(sorted_tasks)
