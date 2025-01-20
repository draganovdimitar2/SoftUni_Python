row_count, column_count = map(int, input().split())

matrix = [input().split() for _ in range(row_count)]
counter = 0

for i in range(len(matrix) - 1):
    for j in range(len(matrix[i]) - 1):
        current_el = matrix[i][j]
        next_el = matrix[i][j + 1]
        down_el = matrix[i + 1][j]
        diagonal_el = matrix[i + 1][j + 1]
        if current_el == next_el == down_el == diagonal_el:
            counter += 1

print(counter)
