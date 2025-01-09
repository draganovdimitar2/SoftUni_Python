text = input()
encrypted_version = ''
for character in text:
    encrypted_version += chr(ord(character) + 3)
print(encrypted_version)
