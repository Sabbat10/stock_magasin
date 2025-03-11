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
def display_products():
    for product in products:
     print(f"{product['name']} - {product['price']} $ - {product['quantity']} en stock")
    
display_products()
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
    
    
# ajouter un produit


def add_product(product_name, product_price, product_quantity):
    new_product = {"name": product_name, "price": product_price, "quantity": product_quantity}
    products.append(new_product)
    print(f"== Le produit {product_name} a été ajouté avec succès. ==")
    
    
Ajouter_produit = input("Entrez le nom du produit que vous souhaitez ajouter : ")
Ajouter_prix = float(input("Entrez le prix du produit que vous souhaitez ajouter : "))
Ajouter_quantite = int(input("Entrez la quantité du produit que vous souhaitez ajouter : "))

add_product(Ajouter_produit, Ajouter_prix, Ajouter_quantite)

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
        
Supprimer_produit = input("Entrez le nom du produit que vous souhaitez supprimer : ")
remove_product(Supprimer_produit)