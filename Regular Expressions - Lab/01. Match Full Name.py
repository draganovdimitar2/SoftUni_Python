import re

regex = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'  # using raw strings so i don't have to double the slashes (because of special characters)
# regex = '\\b[A-Z][a-z]+ [A-Z][a-z]+\\b'  # this will also work
names = input()
matches = re.findall(regex, names)
print(' '.join(names for names in matches))
