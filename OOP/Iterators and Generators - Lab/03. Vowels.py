class vowels:
    VOWELS = ["a", "e", "i", "o", "u"]

    def __init__(self, some_str):
        self.some_str = some_str

        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.idx += 1
        if self.idx >= len(self.some_str):
            raise StopIteration

        char = self.some_str[self.idx]
        if char.lower() in self.VOWELS:
            return char
        return self.__next__()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
