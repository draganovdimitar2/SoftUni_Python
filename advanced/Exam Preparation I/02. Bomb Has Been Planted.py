n, m = [int(x) for x in input().split(', ')]  # dimensions
c_t = [0, 0]
matrix = []
for i in range(n):
    matrix.append(list(input()))
    for j in range(m):
        if matrix[i][j] == 'C':
            c_t = [i, j]

time = 16
commands = {
    'left': [0, -1],
    'right': [0, 1],
    'up': [-1, 0],
    'down': [1, 0]
}

defused = False
killed = False

while time:
    time -= 1
    command = input()

    if command == 'defuse':
        if matrix[c_t[0]][c_t[1]] == 'B':  # if c_t is on the bomb
            time -= 3
            if time >= 0:
                matrix[c_t[0]][c_t[1]] = 'D'
                defused = True
            else:
                matrix[c_t[0]][c_t[1]] = 'X'
            break
        else:  # if c_t is not on the bomb
            time -= 1
    else:  # when moving
        move = commands[command]
        new_row = c_t[0] + move[0]
        new_col = c_t[1] + move[1]
        if 0 <= new_row < n and 0 <= new_col < m:  # if move is within bounds
            if matrix[new_row][new_col] == 'T':
                matrix[new_row][new_col] = '*'
                killed = True
                break
            c_t = [new_row, new_col]

if defused:
    print(f"Counter-terrorist wins!\nBomb has been defused: {time} second/s remaining.")
else:
    print('Terrorists win!')
    if not killed:
        print('Bomb was not defused successfully!')
        print(f"Time needed: {abs(time)} second/s.")

for row in matrix:
    print(''.join(row))
