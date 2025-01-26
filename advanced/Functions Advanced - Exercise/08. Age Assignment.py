def age_assignment(*args, **kwargs):
    result = []
    for name in args:
        age = kwargs.get(name[0])
        result.append(f'{name} is {age} years old.')
    return '\n'.join(sorted(result, key=lambda x: ord(x[0])))


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
