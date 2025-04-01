from .base_store import BaseStore


class ToyStore(BaseStore):
    INITIAL_CAPACITY = 100

    def __init__(self, name: str, location: str):
        super().__init__(name, location, self.INITIAL_CAPACITY)

    @property
    def store_type(self):
        return "ToyStore"

    def store_stats(self):
        result = [f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}",
                  f"{self.get_estimated_profit()}",
                  f"**Toys for sale:"]

        available_toys = {}  # {"toys_model": {count_of_products_of_this_model}}
        average_price_per_model = {}  # {"toys_model": {avg_price_for_this_model}}
        for f in self.products:
            if f.model not in available_toys:
                number_of_products_per_model = len([p for p in self.products if p.model == f.model])
                average_price = (sum([p.price for p in self.products if
                                      p.model == f.model])) / number_of_products_per_model
                available_toys[f.model] = number_of_products_per_model
                average_price_per_model[f.model] = average_price

        sorted_toys_by_model = sorted(available_toys.items(), key=lambda kvp: kvp[0])

        for model, avg_price in sorted_toys_by_model:
            result.append(f"{model}: {avg_price}pcs, average price: {average_price_per_model[model]:.2f}")

        return "\n".join(result)
