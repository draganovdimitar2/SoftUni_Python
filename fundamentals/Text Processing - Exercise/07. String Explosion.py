text = input()
final_string = ''
strength = 0

for index in range(len(text)):
    if strength > 0 and text[index] != '>':  # in case we have an explosion (number)
        strength -= 1
    elif text[index] == '>':  # explosion mark '>'
        final_string += text[index]  # final string += '>'
        strength += int(text[index + 1])
    else:  # no explosion, no explosion mark '>'
        final_string += text[index]

print(final_string)
