def factorial_a(a):
    factorial_a = 1
    if a == 0:
        factorial_a = 1
    else:
        for i in range(1,a+ 1):
            factorial_a = factorial_a*i
            
    return factorial_a

a = int(input())
b = int(input())
first_num = factorial_a(a)
second_num = factorial_a(b)
result = first_num  / second_num
print(f"{result:.2f}")