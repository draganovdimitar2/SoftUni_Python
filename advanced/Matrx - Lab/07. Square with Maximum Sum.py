rows_count, cols_count = list(map(int, input().split(', ')))

matrix = [[int(el) for el in input().split(', ')] for row in range(rows_count)]

max_sum = float("-inf")
sub_matrix = []
for row_index in range(len(matrix) - 1):
    for col_index in range(len(matrix[row_index]) - 1):
        current_el = matrix[row_index][col_index]
        next_el = matrix[row_index][col_index + 1]
        el_below_current = matrix[row_index + 1][col_index]
        el_diagonal_current = matrix[row_index + 1][col_index + 1]
        current_sum = current_el + next_el + el_diagonal_current + el_below_current

        if current_sum > max_sum:
            max_sum = current_sum
            sub_matrix = [
                [current_el, next_el],
                [el_below_current, el_diagonal_current]
            ]
print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)
