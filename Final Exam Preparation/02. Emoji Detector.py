import re

emoji_pattern = r'(::|\*\*)([A-Z]{1}[a-z]{2,})(\1)'
number_pattern = r'\d'
text = input()

emoji_matches = re.finditer(emoji_pattern, text)
number_matches = re.findall(number_pattern, text)

total_num = 1
for number in number_matches:
    total_num = total_num * int(number)

emojis = [emoji.group() for emoji in emoji_matches]  # list of all emojis

cool_emojis = []
for emoji in emojis:
    emoji_coolness = 0  # reset for each emoji
    for char in emoji[2:-2]:  # iterate over each letter of the emoji (not including * or :)
        ascii_val = ord(char)
        emoji_coolness += ascii_val

        if emoji_coolness >= total_num:
            cool_emojis.append(emoji)
            break

print(f"Cool threshold: {total_num}")
print(f"{len(emojis)} emojis found in the text. The cool ones are:")
for cool_emoji in cool_emojis:
    print(cool_emoji)
