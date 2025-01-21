def data_validation(mx, r, c):
    if r < 0 or r >= len(mx) or c < 0 or c >= len(mx[0]):
        return True


def action(mx, add_sub, r, c, value):
    if add_sub == 'Add':
        mx[r][c] += value
    else:
        mx[r][c] -= value
    return mx


rows_count = int(input())
matrix = [list(map(int, input().split())) for el in range(rows_count)]

while True:
    command = input()
    if command == 'END':
        break
    math_action = command.split()[0]
    row_index, col_index, value = list(map(int, command.split()[1:]))
    if data_validation(matrix, row_index, col_index):
        print("Invalid coordinates")
        continue
    action(matrix, math_action, row_index, col_index, value)

[print(*row) for row in matrix]
