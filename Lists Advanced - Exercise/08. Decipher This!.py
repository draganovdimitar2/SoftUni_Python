secret_message = input().split()
decipher = ''
for word in secret_message:
    word = list(word) # convert from str to list
    characters_to_convert = []
    for char in word:
        if char.isdigit():
            characters_to_convert.append(char)
    for char in characters_to_convert:
        if char.isdigit():
            word.remove(char)
    character = "".join(characters_to_convert)
    character = chr(int(character))
    word.insert(0, character)
    word[1], word[-1]=word[-1], word[1]
    word = ''.join(word)
    decipher += word + ' '
print(decipher.strip())