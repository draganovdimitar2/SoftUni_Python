from itertools import product

from .product import Product
from typing import List, Optional


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> Optional[Product]:
        return next((p for p in self.products if p.name == product_name), None)

    def remove(self, product_name):
        product = self.find(product_name)
        if product:
            self.products.remove(product)

    def __repr__(self):
        return "\n".join([f"{p.name}: {p.quantity}" for p in self.products])
