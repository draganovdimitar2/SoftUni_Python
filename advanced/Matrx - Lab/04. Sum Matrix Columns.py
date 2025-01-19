rows_count, cols_count = [int(el) for el in input().split(', ')]
matrix = [[int(el) for el in input().split()] for row in range(rows_count)]

for col_index in range(cols_count):
    current_col_sum = 0
    for row_index in range(rows_count):
        current_col_sum += matrix[row_index][col_index]
    print(current_col_sum)
