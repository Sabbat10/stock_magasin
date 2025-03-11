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

# Afficher les produits

for product in products:
    print(f"{product['name']} - {product['price']} $ - {product['quantity']} en stock")
    

# verifier si un produit est disponible
def is_product_available(product_name):
    for product in products:
        if product['name'] == product_name:
            return True
    return False

rechercher_produit = input("Entrez le nom du produit que vous recherchez : ")

if is_product_available(rechercher_produit.lower()):
    if rechercher_produit.lower() in [product['name'] for product in products]:
        for product in products:
            if product['name'] == rechercher_produit.lower():
                print(f"== Le produit {rechercher_produit.upper()} est disponible ==")
                print(f"Prix : {product['price']} $")
                print(f"Quantité : {product['quantity']} en stock")
                break
            else:
                print(f"Le produit {rechercher_produit} n'est pas disponible")
else:
    print(f"Le produit {rechercher_produit} n'est pas disponible")