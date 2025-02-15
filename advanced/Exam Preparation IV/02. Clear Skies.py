n = int(input())
pos = [0, 0]
enemy_count = 0
matrix = []
for i in range(n):
    matrix.append(list(input()))
    for j in range(n):
        if matrix[i][j] == 'J':
            pos = [i, j]
        elif matrix[i][j] == 'E':
            enemy_count += 1

moves = {'up': [-1, 0], 'down': [1, 0], 'right': [0, 1], 'left': [0, -1]}  # all possible moves}
armor = 300
matrix[pos[0]][pos[1]] = '-'
while True:
    command = input()
    next_row = moves[command][0] + pos[0]
    next_col = moves[command][1] + pos[1]
    pos = [next_row, next_col]

    if matrix[pos[0]][pos[1]] == "E":  # enemy reached
        matrix[pos[0]][pos[1]] = '-'
        if enemy_count > 1:
            enemy_count -= 1
            armor -= 100
            if armor == 0:
                print(f"Mission failed, your jetfighter was shot down! Last coordinates [{next_row}, {next_col}]!")
                break

        else:
            enemy_count -= 1
            print('Mission accomplished, you neutralized the aerial threat!')
            break

    elif matrix[pos[0]][pos[1]] == "R":
        matrix[pos[0]][pos[1]] = '-'
        armor = min(armor + 100, 300)

matrix[pos[0]][pos[1]] = 'J'
[print(*row, sep='') for row in matrix]
