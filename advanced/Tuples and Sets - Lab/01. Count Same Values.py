numbers = tuple(float(el) for el in input().split())

data = {}
for el in numbers:
    data[el] = numbers.count(el)

for k, v in data.items():
    print(f'{k:.1f} - {v} times')
