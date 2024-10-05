N = int(input())

for first_letter in range(97, 97 + N):
    for second_letter in range(97, 97 + N):
        for third_letter in range(97, 97 + N):
            print(f'{chr(first_letter)}{chr(second_letter)}{chr(third_letter)}')