row_count, col_count = [int(x) for x in input().split()]

start = ord('a')

for r in range(row_count):
    for j in range(col_count):
        print(f"{chr(start + r)}{chr(start + r + j)}{chr(start + r)}", end=' ')
    print()
