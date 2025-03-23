def logged(function):
    def wrapper(*args):
        func_name = f"you called {function.__name__}({', '.join(str(el) for el in args)})\n"
        result = function(*args)
        return func_name + f"it returned {result}"

    return wrapper
