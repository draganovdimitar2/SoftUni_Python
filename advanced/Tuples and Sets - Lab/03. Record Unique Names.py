n = int(input())
l = []

for _ in range(n):
    name = input()
    l.append(name)

print('\n'.join({name for name in l}))
