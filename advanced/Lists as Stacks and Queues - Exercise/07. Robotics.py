from collections import deque


def time_to_seconds(time_str):
    h, m, s = map(int, time_str.split(':'))
    return h * 3600 + m * 60 + s


def seconds_to_time(seconds):
    h = (seconds // 3600) % 24
    m = (seconds // 60) % 60
    s = seconds % 60
    return f"{h:02}:{m:02}:{s:02}"


robots_input = input()
start_time = input()
products = deque()

while True:
    product = input()
    if product == "End":
        break
    products.append(product)

robots = []
for robot_info in robots_input.split(';'):
    name, process_time = robot_info.split('-')
    robots.append({'name': name, 'process_time': int(process_time), 'available_at': 0})

current_time = time_to_seconds(start_time)

while products:
    current_time += 1
    product = products.popleft()

    robot_assigned = False
    for robot in robots:
        if current_time >= robot['available_at']:
            robot['available_at'] = current_time + robot['process_time']
            print(f"{robot['name']} - {product} [{seconds_to_time(current_time)}]")
            robot_assigned = True
            break

    if not robot_assigned:
        products.append(product)
