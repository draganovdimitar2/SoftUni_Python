def vowel_filter(function):
    def wrapper():
        result = function()
        return [char for char in result if char in "a, e, i, o, u."]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
