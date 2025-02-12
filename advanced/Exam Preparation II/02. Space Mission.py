n = int(input())
spaceship = [0, 0]
matrix = []
resources = 100  # default value

for i in range(n):
    matrix.append(input().split())
    for j in range(n):
        if matrix[i][j] == 'S':
            spaceship = [i, j]

moves = {'up': [-1, 0], 'down': [1, 0], 'right': [0, 1], 'left': [0, -1]}  # all possible moves
matrix[spaceship[0]][spaceship[1]] = '.'  # make the first spaceship position empty
lost_in_space = False
planet_reached = False

while resources:
    command = input()
    next_row = moves[command][0] + spaceship[0]
    next_col = moves[command][1] + spaceship[1]

    if 0 <= next_row < n and 0 <= next_col < n:  # within matrix boundaries
        resources -= 5
        if matrix[next_row][next_col] == 'R':
            resources = min(resources + 10, 100)
        elif matrix[next_row][next_col] == 'M':
            resources -= 5
            matrix[next_row][next_col] = '.'
        elif matrix[next_row][next_col] == 'P':
            planet_reached = True
            break
        spaceship = [next_row, next_col]  # the last position of the spaceship

    else:  # outside boundaries
        lost_in_space = True
        matrix[spaceship[0]][spaceship[1]] = 'S'
        break

if planet_reached:
    print(f"Mission accomplished! The spaceship reached Planet B with {resources} resources left.")
else:
    if resources < 5:
        print(f"Mission failed! The spaceship was stranded in space.")
    elif lost_in_space:
        print("Mission failed! The spaceship was lost in space.")
    matrix[spaceship[0]][spaceship[1]] = 'S'
for row in matrix:
    print(*row, sep=' ')
