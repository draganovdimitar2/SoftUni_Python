import re

pattern = r'\bwww\.[a-zA-Z0-9-]+\.[a-z]+(\.[a-z]+)*\b'
text = input()
matches = re.findall(pattern, text)
for match in matches:
    print('printing matches: ', match)

