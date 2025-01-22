n = int(input())

Alice = []
matrix = []
for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == 'A':
            matrix[row][col] = '*'  # making the Alice starting position as '*'
            Alice = [row, col]

possible_directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
tea_count = 0
row = Alice[0]
col = Alice[1]

while tea_count < 10:
    command = input()
    row += possible_directions[command][0]
    col += possible_directions[command][1]
    if 0 > row or row >= n or 0 > col or col >= n:
        break
    if matrix[row][col] == 'R':
        matrix[row][col] = '*'
        break
    if matrix[row][col].isdigit():
        tea_count += int(matrix[row][col])
    matrix[row][col] = '*'

if tea_count >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

[print(*row) for row in matrix]
