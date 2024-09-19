first_name = input()
second_name = input()
counter = 0
first_letters = ''
for char in second_name:
    last_letters = first_name[counter+1:]
    first_letters += char

    if counter == 0:
        if char == first_name[counter]:
            new_word = char + last_letters
        else:
            new_word = char + last_letters
            print(new_word)
    else:
        if char == first_name[counter]:
            new_word = first_letters + last_letters
        else:
            new_word = first_letters + last_letters
            print(new_word)

    counter += 1