str_input = input().split(' ')
mydict = {}

for word in str_input:
    for char in word:
        if char in mydict:
            mydict[char] += 1
        else:
            mydict[char] = 1

for key, value in mydict.items():
    print(f'{key} -> {value}')
