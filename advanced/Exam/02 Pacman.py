n = int(input())
pos = [0, 0]
health = 100
stars_count = 0
matrix = []
for i in range(n):
    matrix.append(list(input()))
    for j in range(n):
        if matrix[i][j] == 'P':
            pos = [i, j]
        elif matrix[i][j] == '*':
            stars_count += 1

moves = {'up': [-1, 0], 'down': [1, 0], 'right': [0, 1], 'left': [0, -1]}  # all possible moves
matrix[pos[0]][pos[1]] = '-'  # mark the starting pos wit a dash
immunity = False
outside_boundaries = False
while True:
    command = input()
    if command == 'end':
        break

    next_row = moves[command][0] + pos[0]
    next_col = moves[command][1] + pos[1]

    if not 0 <= next_row < n or not 0 <= next_col < n:  # outside boundaries
        outside_boundaries = True
        if next_row < 0:
            pos[0] = n - 1
        if next_row > n - 1:
            pos[0] = 0
        if next_col < 0:
            pos[1] = n - 1
        if next_col > n - 1:
            pos[1] = 0
    if not outside_boundaries:
        pos = [next_row, next_col]  # update position
    outside_boundaries = False

    if matrix[pos[0]][pos[1]] == '*':
        stars_count -= 1
        matrix[pos[0]][pos[1]] = '-'
        if stars_count == 0:
            break
    elif matrix[pos[0]][pos[1]] == 'G':
        if not immunity:
            health -= 50
            matrix[pos[0]][pos[1]] = '-'
            if health <= 0:
                break
        else:
            immunity = False
            matrix[pos[0]][pos[1]] = '-'
    elif matrix[pos[0]][pos[1]] == 'F':
        matrix[pos[0]][pos[1]] = '-'
        immunity = True

matrix[pos[0]][pos[1]] = 'P'
if health > 0:
    if stars_count == 0:
        print("Pacman wins! All the stars are collected.")
    else:
        print("Pacman failed to collect all the stars.")

else:
    print(f"Game over! Pacman last coordinates [{pos[0]},{pos[1]}]")

print(f"Health: {health}")
if stars_count:
    print(f"Uncollected stars: {stars_count}")
[print(*row, sep='') for row in matrix]
