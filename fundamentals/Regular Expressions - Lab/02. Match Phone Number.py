import re

numbers = input()
pattern = r'\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b'
# pattern = '\\+359-2-\\d{3}-\\d{4}\\b|\\+359 2 \\d{3} \\d{4}\\b'  # this will also work
valid_numbers = re.findall(pattern, numbers)
print(', '.join(valid_numbers))
