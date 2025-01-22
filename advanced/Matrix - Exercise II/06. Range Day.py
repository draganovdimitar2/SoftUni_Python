n = 5  # we have matrix 5x5
position = []
targets_count = 0
defeated_targets = 0
targets_submatrix = []
possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

matrix = []
for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == 'A':
            position = [int(row), int(col)]
        elif matrix[row][col] == 'x':
            targets_count += 1

num = int(input())

for _ in range(num):
    command = input().split()
    action = command[0]
    direction = command[1]
    if action == 'move':
        steps = int(command[2])
        new_row = position[0] + possible_moves[direction][0] * steps
        new_col = position[1] + possible_moves[direction][1] * steps
        if 0 <= new_row < n and 0 <= new_col < n and matrix[new_row][new_col] == '.':
            matrix[new_row][new_col] = 'A'
            matrix[position[0]][position[1]] = '.'
            position = [new_row, new_col]

    else:  # action == 'shoot
        bullet_row = possible_moves[direction][0] + position[0]
        bullet_col = possible_moves[direction][1] + position[1]
        while 0 <= bullet_row < n and 0 <= bullet_col < n:
            if matrix[bullet_row][bullet_col] == 'x':
                targets_submatrix.append([bullet_row, bullet_col])
                defeated_targets += 1
                matrix[bullet_row][bullet_col] = '.'
                break
            bullet_row += possible_moves[direction][0]
            bullet_col += possible_moves[direction][1]

        if defeated_targets == targets_count:
            print(f"Training completed! All {targets_count} targets hit.")
            break

if defeated_targets != targets_count:
    print(f'Training not completed! {targets_count - defeated_targets} targets left.')
[print(row) for row in targets_submatrix]
