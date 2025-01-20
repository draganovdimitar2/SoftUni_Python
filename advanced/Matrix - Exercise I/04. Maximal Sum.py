row_count, column_count = map(int, input().split())
matrix = [[int(x) for x in input().split()] for _ in range(row_count)]
max_num = float("-inf")
max_row = 0
max_col = 0
for row in range(row_count - 2):
    for col in range(column_count - 2):
        total_sum = 0
        for r in range(row, row + 3):
            for c in range(col, col + 3):
                total_sum += matrix[r][c]
        if total_sum > max_num:
            max_num = total_sum
            max_row = row
            max_col = col

print(f"Sum = {max_num}")
max_submatrix = [matrix[r][max_col:max_col + 3] for r in range(max_row, max_row + 3)]
[print(*row) for row in max_submatrix]
