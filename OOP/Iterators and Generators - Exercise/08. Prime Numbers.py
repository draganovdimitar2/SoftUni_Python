from math import sqrt


def get_primes(some_list: list):
    result = []
    for n in some_list:
        if n < 2:
            continue
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                break
        else:
            yield n


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
