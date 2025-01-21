n = int(input())

matrix = []
knights = []  # [[row_index, col_index], [row_index, col_index]...]
# using for loop so we can save each knight index in var
for row in range(n):
    matrix.append([x for x in input()])
    for col in range(n):
        if matrix[row][col] == 'K':  # knight check
            knights.append([row, col])

removed_knights = 0
possible_movies = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]
while True:
    max_hits = 0
    max_knight = [0, 0]  # list for the knight with max hits (will be override)

    for k_row, k_col in knights:
        hits = 0
        for move in possible_movies:
            next_row = k_row + move[0]
            next_col = k_col + move[1]
            if 0 <= next_row < n and 0 <= next_col < n:
                if matrix[next_row][next_col] == 'K':
                    hits += 1
        if hits > max_hits:
            max_hits = hits
            max_knight = [k_row, k_col]

    if max_hits == 0:  # if there are no hits, break
        break
    knights.remove(max_knight)
    matrix[max_knight[0]][max_knight[1]] = '0'
    removed_knights += 1

print(removed_knights)
