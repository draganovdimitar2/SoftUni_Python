data = input().split()

while True:
    command = input()

    if command == "3:1":
        break

    parts = command.split()
    action = parts[0]

    if action == "merge":
        start_index = int(parts[1])
        end_index = int(parts[2])

        start_index = max(0, start_index)
        end_index = min(len(data) - 1, end_index)

        merged = ''.join(data[start_index:end_index + 1])
        data = data[:start_index] + [merged] + data[end_index + 1:]

    elif action == "divide":
        index = int(parts[1])
        partitions = int(parts[2])

        if 0 <= index < len(data):
            element = data[index]
            part_length = len(element) // partitions
            divided = []

            for i in range(partitions - 1):
                divided.append(element[i * part_length:(i + 1) * part_length])
            divided.append(element[(partitions - 1) * part_length:])

            data = data[:index] + divided + data[index + 1:]

print(' '.join(data))
