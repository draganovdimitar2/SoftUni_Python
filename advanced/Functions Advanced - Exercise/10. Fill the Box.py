def fill_the_box(*args):
    box_size = args[0] * args[1] * args[2]
    remaining_cubes = 0
    for arg in args[3:]:
        if arg == 'Finish':
            break
        if box_size >= arg:
            box_size -= arg
        else:
            remaining_cubes += arg - box_size
            box_size = 0

    if box_size:
        return f"There is free space in the box. You could put {box_size} more cubes."
    else:
        return f"No more free space! You have {remaining_cubes} more cubes."
