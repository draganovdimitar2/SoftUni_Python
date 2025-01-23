def sorting_cheeses(**kwargs):
    sorted_data = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    result = ''
    for cheese_name, quantity in sorted_data:
        result += cheese_name + "\n"
        for el in sorted(quantity, reverse=True):
            result += f"{el}\n"
    return result
