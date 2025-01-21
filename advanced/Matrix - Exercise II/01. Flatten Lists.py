strings = input().split('|')

matrix = []

for i in range(len(strings) - 1, -1, -1):
    row = strings[i].split()
    if row:
        matrix.append(row)

[print(*row, end=' ') for row in matrix]
