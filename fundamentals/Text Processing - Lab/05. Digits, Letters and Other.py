text = input()
digits = ''
letters = ''
special_chars = ''

for char in text:
    if char.isdigit():
        digits += char
    elif char.isalpha():
        letters += char
    else:
        special_chars += char

print(digits)
print(letters)
print(special_chars)
