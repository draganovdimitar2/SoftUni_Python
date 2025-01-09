import re

text = input()
pattern = r'\s((([a-z0-9]+)[\.\_\-a-z0-9]*)@([a-z\-]+)(\.[a-z]+)+)\b'
matched_emails = re.findall(pattern, text)
for email in matched_emails:
    print(email[0])
