text = input()
char_storage = set()

for char in text:
    char_storage.add(char)

for char in sorted(char_storage):
    print(f'{char}: {text.count(char)} time/s')
