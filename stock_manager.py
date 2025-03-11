# listes des produits disponibles
products = [
    {"name": "pomme", "price": 1.0, "quantity": 10},
    {"name": "poire", "price": 1.2, "quantity": 5},
    {"name": "banane", "price": 1.5, "quantity": 8},
    {"name": "orange", "price": 1.8, "quantity": 7},
    {"name": "ananas", "price": 2.0, "quantity": 6},
    {"name": "kiwi", "price": 2.0, "quantity": 6},
]

print("=" * 50)
print("Liste des produits disponibles")

for product in products:
    print(f"{product['name']} - {product['price']} $ - {product['quantity']} en stock")