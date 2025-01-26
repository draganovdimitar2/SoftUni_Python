def concatenate(*args, **kwargs):
    result = ''.join(args)
    for k, v in kwargs.items():
        result = result.replace(k, v)
    return result
