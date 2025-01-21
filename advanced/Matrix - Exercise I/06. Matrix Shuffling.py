def coordinates_validation_fail(action, coordinates):
    if action != 'swap' or len(coordinates) != 4:
        return "Invalid input!"
    first_row, first_col, second_row, second_col = coordinates
    if first_row < 0 or second_row < 0 or first_col < 0 or second_col < 0:
        return "Invalid input!"
    if first_row not in range(rows_count) or first_col not in range(col_count) or second_row not in range(
            rows_count) or second_col not in range(col_count):
        return "Invalid input!"
    return False


def coordinates_swapping(mx, a, b, c, d):
    mx[a][b], mx[c][d] = mx[c][d], mx[a][b]
    return mx


rows_count, col_count = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows_count)]

while True:
    command = input()
    if command == 'END':
        break
    command = command.split()

    try:
        coordinates = list(map(int, command[1:]))
    except ValueError:
        print("Invalid input!")
        continue

    coordinates_check = coordinates_validation_fail(command[0], coordinates)
    if coordinates_check:
        print(coordinates_check)
        continue
    else:
        first_row, first_col, second_row, second_col = coordinates
        coordinates_swapping(matrix, first_row, first_col, second_row, second_col)
        [print(*row) for row in matrix]
