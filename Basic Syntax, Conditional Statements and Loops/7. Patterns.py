# First way
n = int(input())

for i in range(1, n+1):
    print('*' * i)

for i in range(n-1, 0, -1):
    print('*' * i)

# Second way
num = int(input())
star = ''

for i in range(1, num + 1):
    star += '*'
    print(star)

for i in range(num - 1, 0, -1):
    star = star[:-1]
    print(star)

# Third way
num = int(input())
star = '*'

for column in range(1, num + 1):
    print(star)
    star = star + '*'
else:
    star = star[1:]
    for row in range(num, 0, -1):
        star = star[1:]
        print(star)