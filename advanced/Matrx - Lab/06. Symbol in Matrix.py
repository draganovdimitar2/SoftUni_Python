n = int(input())

matrix = []
for _ in range(n):
    raw_data = [char for char in input()]
    matrix.append(raw_data)
symbol = input()

for row_index in range(len(matrix)):
    for column_index in range(len(matrix[row_index])):
        if matrix[row_index][column_index] == symbol:
            print(f"({row_index}, {column_index})")
            exit()

else:
    print(f"{symbol} does not occur in the matrix")
