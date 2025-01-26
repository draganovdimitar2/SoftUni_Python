def even_odd(*args):
    if args[-1] == 'even':
        return [el for el in map(int, args[:-1]) if el % 2 == 0]
    return [el for el in map(int, args[:-1]) if el % 2 != 0]
