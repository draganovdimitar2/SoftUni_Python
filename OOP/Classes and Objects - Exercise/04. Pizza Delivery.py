class PizzaDelivery:
    def __init__(self, name: str, price: float, ingredients: dict, ordered: bool = False):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = ordered

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        if ingredient in self.ingredients:
            self.ingredients[ingredient] += quantity
        else:
            self.ingredients[ingredient] = quantity
        self.price += quantity * price_per_quantity

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        if ingredient in self.ingredients:
            if self.ingredients[ingredient] < quantity:
                return f"Please check again the desired quantity of {ingredient}!"
            self.ingredients[ingredient] -= quantity
            self.price -= quantity * price_per_quantity
        else:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"

    def make_order(self):
        self.ordered = True
        ingredients_list = [f"{k}: {v}" for k, v in self.ingredients.items()]
        ingredients_str = ", ".join(ingredients_list)
        return f"You've ordered pizza {self.name} prepared with {ingredients_str} and the price will be {self.price}lv."
