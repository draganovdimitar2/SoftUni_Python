n = int(input())  # size of the field (a square matrix)
player_pos = [0, 0]
stars_counter = 2  # player always starts with 2 stars
matrix = []
for i in range(n):
    matrix.append(input().split())
    for j in range(n):
        if matrix[i][j] == 'P':  # find the player starting position
            player_pos = [i, j]

moves = {'up': [-1, 0], 'down': [1, 0], 'right': [0, 1], 'left': [0, -1]}  # all possible moves}

matrix[player_pos[0]][player_pos[1]] = '.'  # mark player's starting position as a dot
game_win = False
while True:  # if player lose his stars, the game ends
    command = input()
    next_row = moves[command][0] + player_pos[0]
    next_col = moves[command][1] + player_pos[1]

    if 0 <= next_row < n and 0 <= next_col < n:  # if the player is within the matrix boundaries
        if matrix[next_row][next_col] == '#':  # when player hit an obstacle he lose a star
            stars_counter -= 1
        else:
            if matrix[next_row][next_col] == '*':  # when collect a star, mark the place with a dot
                matrix[next_row][next_col] = '.'
                stars_counter += 1
            player_pos = [next_row, next_col]  # update player pos
    else:  # outside of the game boundaries
        if matrix[0][0] == '*':
            stars_counter += 1
            matrix[0][0] = '.'
        player_pos = [0, 0]

    if stars_counter <= 0:
        break
    elif stars_counter >= 10:
        game_win = True  # the player wins
        break

if game_win:
    print("You won! You have collected 10 stars.")
else:
    print("Game over! You are out of any stars.")
matrix[player_pos[0]][player_pos[1]] = 'P'  # mark the player's final position as P
print(f"Your final position is [{player_pos[0]}, {player_pos[1]}]")
for row in matrix:
    print(*row, sep=' ')
