n = int(input())
storage = set()

for _ in range(n):
    element = input().split()
    while element:
        storage.add(element.pop())

print(*storage, sep = '\n')