N = int(input())
total_sum = 0

for lines in range(N):
    letter = input()
    total_sum += ord(letter)

print(f'The sum equals: {total_sum}')