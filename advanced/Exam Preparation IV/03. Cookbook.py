def cookbook(*args):
    recipes_by_cuisine = {}
    ingredients_by_recipe = {}
    result = []
    for recipe, cuisine, ingredients in args:
        if cuisine not in recipes_by_cuisine:
            recipes_by_cuisine[cuisine] = []
        recipes_by_cuisine[cuisine].append(recipe)

    for recipe, cuisine, ingredients in args:
        if recipe not in ingredients_by_recipe:
            ingredients_by_recipe[recipe] = []
        ingredients_by_recipe[recipe].append(ingredients)

    sorted_recipes = dict(sorted(recipes_by_cuisine.items(), key=lambda x: (-len(x[1]), x[0])))
    for cuisine, recipes in sorted_recipes.items():
        result.append(f"{cuisine} cuisine contains {len(recipes)} recipes:")
        for recipe in sorted(recipes):
            result.append(
                f"  * {recipe} -> Ingredients: {', '.join(str(el) for el in ingredients_by_recipe[recipe][0])}")
    return "\n".join(row for row in result)
