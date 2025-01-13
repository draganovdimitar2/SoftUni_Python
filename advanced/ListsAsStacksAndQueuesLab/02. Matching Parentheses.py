expression = input()
stack = []

for index in range(len(expression)):
    if expression[index] == "(":
        stack.append(index)  # append each open parenthesis index in stack
    elif expression[index] == ')':
        start_index = stack.pop()  # pop the last open parenthesis index from the stack
        end_index = index + 1
        print(expression[start_index:end_index])
