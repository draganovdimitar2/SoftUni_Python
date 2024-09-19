inputs_num = int(input())

for num in range(inputs_num):
    num = int(input())
    if num % 2 == 1:
        print(f"{num} is odd!")
        break
else:
    print('All numbers are even.')