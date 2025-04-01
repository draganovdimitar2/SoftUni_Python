from project.stores.base_store import BaseStore


class FurnitureStore(BaseStore):
    INITIAL_CAPACITY = 50

    def __init__(self, name: str, location: str):
        super().__init__(name, location, self.INITIAL_CAPACITY)

    @property
    def store_type(self):
        return "FurnitureStore"

    def store_stats(self):
        result = [f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}",
                  f"{self.get_estimated_profit()}",
                  f"**Furniture for sale:"]

        available_furniture = {}  # {"furniture_model": {count_of_products_of_this_model}}
        average_price_per_model = {}  # {"furniture_model": {avg_price_for_this_model}}
        for f in self.products:
            if f.model not in available_furniture:
                number_of_products_per_model = len([p for p in self.products if p.model == f.model])
                average_price = (sum([p.price for p in self.products if
                                      p.model == f.model])) / number_of_products_per_model
                available_furniture[f.model] = number_of_products_per_model
                average_price_per_model[f.model] = average_price

        sorted_furniture_by_model = sorted(available_furniture.items(), key=lambda kvp: kvp[0])

        for model, avg_price in sorted_furniture_by_model:
            result.append(f"{model}: {avg_price}pcs, average price: {average_price_per_model[model]:.2f}")

        return "\n".join(result)
