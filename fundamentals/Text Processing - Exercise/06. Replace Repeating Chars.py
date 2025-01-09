passed_chars = ''
text = input()
for char in text:
    try:
        passed_chars[-1]
    except IndexError:
        passed_chars += char
    else:
        if char == passed_chars[-1]:
            continue
        else:
            passed_chars += char
print(passed_chars)
