def list_roman_emperors(*args, **kwargs):
    successful_emperors = {}
    unsuccessful_emperors = {}
    for name, status in args:
        if status:  # if status == True
            successful_emperors[name] = kwargs[
                name]  # we add the emperor name as a key and his years of rule as a value
        else:
            unsuccessful_emperors[name] = kwargs[name]

    result = [f"Total number of emperors: {len(args)}"]  # we will add more items to this result later
    if successful_emperors:  # if we have successful emperors
        result.append("Successful emperors:")
        successful_emperors_sorted = sorted(successful_emperors.items(), key=lambda x: (-x[1], x[0]))
        for name, year in successful_emperors_sorted:
            result.append(f"****{name}: {year}")

    if unsuccessful_emperors:  # if we have unsuccessful emperors
        result.append('Unsuccessful emperors:')
        unsuccessful_emperors_sorted = sorted(unsuccessful_emperors.items(), key=lambda x: (x[1], x[0]))
        for name, year in unsuccessful_emperors_sorted:
            result.append(f"****{name}: {year}")

    return "\n".join(result)
