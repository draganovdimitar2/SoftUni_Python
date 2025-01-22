presents_count = int(input())
n = int(input())

nice_kids = 0
santa_position = []
possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

matrix = []
for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == 'S':
            santa_position = [int(row), int(col)]
        elif matrix[row][col] == 'V':
            nice_kids += 1

all_nice_kids = nice_kids
for _ in range(len(matrix)):
    command = input()
    if command == "Christmas morning":
        break
    elif command in possible_moves:
        row = santa_position[0] + possible_moves[command][0]
        col = santa_position[1] + possible_moves[command][1]
        if 0 <= row < n and 0 <= col < n:
            matrix[santa_position[0]][santa_position[1]] = '-'
            santa_position = [row, col]
            if matrix[row][col] == 'V':  # a nice kid
                nice_kids -= 1
                presents_count -= 1
                matrix[row][col] = '-'
                if presents_count == 0 and nice_kids:
                    print("Santa ran out of presents!")
                    break
            elif matrix[row][col] == 'X':
                matrix[row][col] = '-'
            elif matrix[row][col] == 'C':
                matrix[row][col] = 'S'
                for position in possible_moves:
                    r = possible_moves[position][0] + row
                    c = possible_moves[position][1] + col
                    if matrix[r][c] == 'V':
                        presents_count -= 1
                        nice_kids -= 1
                        matrix[r][c] = '-'
                    if matrix[r][c] == 'X':
                        presents_count -= 1
                        matrix[r][c] = '-'
                    if presents_count == 0 and nice_kids:
                        print("Santa ran out of presents!")
                        break
            else:
                matrix[santa_position[0]][santa_position[1]] = 'S'
    if presents_count == 0:
        break
matrix[santa_position[0]][santa_position[1]] = 'S'

[print(*row) for row in matrix]
if nice_kids:
    print(f"No presents for {nice_kids} nice kid/s.")
else:
    print(f"Good job, Santa! {all_nice_kids} happy nice kid/s.")
