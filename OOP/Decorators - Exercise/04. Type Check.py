def type_check(var_type):
    def decorator(function):
        def wrapper(char):
            if isinstance(char, var_type):
                return function(char)
            return "Bad Type"

        return wrapper

    return decorator
