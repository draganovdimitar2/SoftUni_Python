data = input().split(', ')
row_count = int(data[0])
column_count = int(data[1])
matrix_sum = 0
matrix = []

for row_index in range(row_count):
    data_row = [int(el) for el in input().split(', ')]
    matrix.append(data_row)

for row_index in range(row_count):
    for el in matrix[row_index]:
        matrix_sum += el

# for row_index in range(len(matrix)):
#     for col_index in range(len(matrix[row_index])):
#         matrix_sum += matrix[row_index][col_index]

print(matrix_sum)
print(matrix)
