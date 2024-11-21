import re

usernames = input()
pattern = r'[\w\-]+'
matches = re.findall(pattern, usernames)
usernames = usernames.split(', ')
print('\n'.join(username for username in usernames if username in matches and 3 <= len(username) <= 16))
