two_str = input()
first_word, second_word = two_str.split()
total_sum = 0
if len(first_word) == len(second_word):
    for i in range(len(first_word)):
        total_sum += ord(first_word[i]) * ord(second_word[i])
elif len(first_word) > len(second_word):
    for i in range(len(second_word)):
        total_sum += ord(first_word[i]) * ord(second_word[i])
    for chr in first_word[len(second_word):]:
        total_sum += ord(chr)
else:
    for i in range(len(first_word)):
        total_sum += ord(first_word[i]) * ord(second_word[i])
    for chr in second_word[len(first_word):]:
        total_sum += ord(chr)
print(total_sum)
