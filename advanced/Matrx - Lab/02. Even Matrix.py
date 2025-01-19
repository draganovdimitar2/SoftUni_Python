rows_num = int(input())
matrix = []

for _ in range(rows_num):
    row = [int(el) for el in input().split(', ')]
    matrix.append(row)

matrix = [[el for el in matrix[row_index] if el%2==0]for row_index in range(rows_num)]
print(matrix)
