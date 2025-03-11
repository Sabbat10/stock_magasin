# listes des produits disponibles
from tabulate import tabulate
products = [
    {"name": "pomme", "price": 1.0, "quantity": 10},
    {"name": "poire", "price": 1.2, "quantity": 5},
    {"name": "banane", "price": 1.5, "quantity": 8},
    {"name": "orange", "price": 1.8, "quantity": 7},
    {"name": "ananas", "price": 2.0, "quantity": 6},
    {"name": "kiwi", "price": 2.0, "quantity": 6},
]

print("=" * 50)
print("GESTIONS DE MAGASIN")
print("Taper : ")

# Afficher les produits
def display_products():
    print("Voici la liste des produits disponibles :")
    headers = {
        "name": "Nom",
        "price": "Prix ($)",
        "quantity": "Quantité"
    }
    print(tabulate(products, headers=headers, tablefmt="grid"))

# verifier si un produit est disponible
def is_product_available(product_name):
    for product in products:
        if product['name'] == product_name:
            return True
    return False
  
# ajouter un produit
def add_product(product_name, product_price, product_quantity):
    new_product = {"name": product_name, "price": product_price, "quantity": product_quantity}
    products.append(new_product)
    print(f"== Le produit {product_name} a été ajouté avec succès. ==")
    display_products()

# supprimer un produit

def remove_product(product_name):
    for product in products:
        if product['name'] == product_name:
            products.remove(product)
            print(f"== Le produit {product_name} a été supprimé avec succès. ==")
            display_products()
            break
    else:
        print(f"Le produit {product_name} n'a pas été trouvé.")
        
