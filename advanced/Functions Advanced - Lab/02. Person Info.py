def get_info(**kwargs):
    info = []
    for k, v in kwargs.items():
        info.append(v)
    return f"This is {info[0]} from {info[1]} and he is {info[2]} years old"
