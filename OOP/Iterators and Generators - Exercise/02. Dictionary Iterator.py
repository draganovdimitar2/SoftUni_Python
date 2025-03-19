class dictionary_iter:
    def __init__(self, obj: dict):
        self.obj = tuple(obj.items())
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.obj):
            i = self.i
            self.i += 1
            return self.obj[i]
        raise StopIteration
