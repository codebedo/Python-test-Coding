from dataclasses import  dataclass
from typing import  List


@dataclass
class Product:
    name : str
    category: str
    price : float


products = [
    Product("Asus Laptop", "computer", 7500),
    Product("HP Laptop", "computer", 6700),
    Product("Iphone 13", "phone", 2000),
    Product("Macbokk", "Computer", 9000),
    Product("Samsung s23", "phone", 2000)
]



filtered = list(filter(lambda p: p.category == "computer", products))


sorted_products = sorted(filtered, key=lambda p: p.price)


for p in sorted_products:
    print(f"{p.name} - {p.price}$")
