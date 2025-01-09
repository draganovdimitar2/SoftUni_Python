parts = input().split('.')
n1, n2, n3 = map(int, parts)
n3 += 1

if n3 > 9:
    n3 = 0
    n2 += 1

if n2 > 9:
    n2 = 0
    n1 += 1

new_version = f"{n1}.{n2}.{n3}"
print(new_version)
