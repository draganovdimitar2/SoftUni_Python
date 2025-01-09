import re

pattern = r'^(\$|\%)([A-Z][a-z]{2,})\1: \[(\d+)\]\|\[(\d+)\]\|\[(\d+)\]\|$'

inputs_count = int(input())

for _ in range(inputs_count):
    text = input()
    matches = re.findall(pattern, text)

    if matches:
        tag = matches[0][1]
        third_number = chr(int(matches[0][-1]))
        second_number = chr(int(matches[0][-2]))
        first_number = chr(int(matches[0][-3]))
        decryptedMessage = first_number + second_number + third_number
        print(f"{tag}: {decryptedMessage}")

    else:
        print("Valid message not found!")
