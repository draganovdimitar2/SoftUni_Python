def action(operator):
    if operator == 'multiply':
        return first_num * second_num
    
    elif operator == 'divide':
        return int(first_num / second_num)
    
    elif operator == 'add':
        return first_num + second_num
    
    else:
        return first_num - second_num


operator = input()
first_num = int(input())
second_num = int(input())
print(action(operator))