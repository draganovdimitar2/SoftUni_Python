n = int(input())
storage = set()

for _ in range(n):
    name = input()
    storage.add(name)

print("\n".join(name for name in storage))
