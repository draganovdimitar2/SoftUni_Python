def plant_garden(arg, *args, **kwargs):
    allowed_plants = {name: quantity for name, quantity in args}
    planted_plants = {}
    for name, quantity in sorted(kwargs.items()):
        if name not in allowed_plants:
            continue
        space_per_plant = allowed_plants[name]
        max_possible_plants = int(arg / space_per_plant)  # how many pcs can fit
        plants_to_plant = min(max_possible_plants, quantity)  # determine how many pcs to plant

        if plants_to_plant > 0:
            planted_plants[name] = plants_to_plant  # Record planted plants
            arg -= plants_to_plant * space_per_plant
        if arg <= 0.0:
            break

    result = ["Planted plants:"]
    [result.append(f"{plant_type}: {planted_plants[plant_type]}") for plant_type in sorted(planted_plants)]
    formated_planted_pcs = "\n".join(result)

    if all(planted_plants.get(pt, 0) == qty for pt, qty in kwargs.items() if pt in allowed_plants):
        return f"All plants were planted! Available garden space: {arg:.1f} sq meters.\n{formated_planted_pcs}"
    return f"Not enough space to plant all requested plants!\n{formated_planted_pcs}"


print(plant_garden(2.0, ("rose", 2.5), ("tulip", 1.2), ("daisy", 0.2), rose=4, tulip=15, sunflower=3, daisy=4))
