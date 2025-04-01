from typing import List, Type
from project.products.base_product import BaseProduct
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.base_store import BaseStore
from project.stores.toy_store import ToyStore
from project.stores.furniture_store import FurnitureStore


class FactoryManager:
    VALID_PRODUCT_TYPES: List[Type[BaseProduct]] = [Chair, HobbyHorse]
    VALID_STORE_TYPES: List[Type[BaseStore]] = [FurnitureStore, ToyStore]

    def __init__(self, name: str):
        self.name = name
        self.income: float = 0.0
        self.products: List[Type[BaseProduct]] = []
        self.stores: List[Type[BaseStore]] = []

    def produce_item(self, product_type: str, model: str, price: float):
        product_class = next((p for p in self.VALID_PRODUCT_TYPES if p.__name__ == product_type), None)

        if product_class is None:
            raise Exception("Invalid product type!")
        product = product_class(model, price)
        self.products.append(product)
        return f"A product of sub-type {product.sub_type} was produced."

    def register_new_store(self, store_type: str, name: str, location: str):
        store_class = next((s for s in self.VALID_STORE_TYPES if s.__name__ == store_type), None)

        if store_class is None:
            raise Exception(f"{store_type} is an invalid type of store!")
        store = store_class(name, location)
        self.stores.append(store)
        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):
        if store.capacity < len(products):
            return f"Store {store.name} has no capacity for this purchase."

        products_for_this_store = [p for p in products if p.sub_type.lower() in store.store_type.lower()]

        if products_for_this_store:
            products_sum_price = 0
            for product in products_for_this_store:
                store.products.append(product)
                self.products.remove(product)
                store.capacity -= 1
                products_sum_price += product.price

            self.income += products_sum_price
            return f"Store {store.name} successfully purchased {len(products_for_this_store)} items."
        return "Products do not match in type. Nothing sold."

    def unregister_store(self, store_name: str):
        store = next((s for s in self.stores if s.name == store_name), None)
        if store is None:
            raise Exception("No such store!")
        if len(store.products) > 0:
            return "The store is still having products in stock! Unregistering is inadvisable."

        self.stores.remove(store)
        return f"Successfully unregistered store {store_name}, location: {store.location}."

    def discount_products(self, product_model: str):
        discounted_products = [p for p in self.products if p.model == product_model]
        [p.discount() for p in discounted_products]
        return f"Discount applied to {len(discounted_products)} products with model: {product_model}"

    def request_store_stats(self, store_name: str):
        store = next((s for s in self.stores if s.name == store_name), None)
        if store is None:
            return "There is no store registered under this name!"
        return store.store_stats()

    def statistics(self):
        product_counts_per_model = {}
        total_price = 0.0
        for product in self.products:
            product_counts_per_model[product.model] = product_counts_per_model.get(product.model, 0) + 1
            total_price += product.price

        stats = [
            f"Factory: {self.name}",
            f"Income: {self.income:.2f}",
            "***Products Statistics***",
            f"Unsold Products: {len(self.products)}. Total net price: {total_price:.2f}"
        ]
        for model in sorted(product_counts_per_model.keys()):
            stats.append(f"{model}: {product_counts_per_model[model]}")

        stats.append(f"***Partner Stores: {len(self.stores)}***")
        for store in sorted(self.stores, key=lambda s: s.name):
            stats.append(store.name)

        return "\n".join(stats).strip()
