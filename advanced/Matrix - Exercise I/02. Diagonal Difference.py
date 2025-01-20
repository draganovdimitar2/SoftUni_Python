n = int(input())

matrix = [[int(el) for el in input().split()] for row in range(n)]
primary_diagonal = sum([matrix[i][i] for i in range(n)])
secondary_diagonal = sum([matrix[i][-1 - i] for i in range(n)])

print(abs(primary_diagonal - secondary_diagonal))
