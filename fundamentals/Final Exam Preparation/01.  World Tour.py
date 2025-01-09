def add_stop(stops: str, index: int, string: str) -> str:
    if index in range(len(stops)):
        stops = stops[:index] + string + stops[index:]
    return stops


def remove_stops(stops: str, start_index: int, end_index: int) -> str:
    if start_index in range(len(stops)) and end_index in range(len(stops)):
        stops = stops[:start_index] + stops[end_index + 1:]
    return stops


def switch(stops: str, old_string: str, new_string: str) -> str:
    if old_string in stops:
        stops = stops.replace(old_string, new_string)
    return stops


stops = input()
command = input()

while command != 'Travel':
    command = command.split(':')
    if command[0] == 'Add Stop':
        index, string = int(command[1]), command[-1]
        stops = add_stop(stops, index, string)
    elif command[0] == 'Remove Stop':
        start_index, end_index = int(command[1]), int(command[2])
        stops = remove_stops(stops, start_index, end_index)
    else:
        old_string, new_string = command[1], command[2]
        new_stops = switch(stops, old_string, new_string)
        if new_stops:  # if it is not None
            stops = new_stops

    print(stops)
    command = input()

print(f"Ready for world tour! Planned stops: {stops}")
