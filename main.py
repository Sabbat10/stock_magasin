
from stock_manager import *

while True:
    choice_operation = input("1 - voir les produits\n2 - ajouter un produit\n3 - supprimer un produit\n4 - rechercher un produit\n5 - quitter\n:")
    
    print("")
    
    # afficher produit
    if choice_operation == "1":
        display_products()
        
    # ajouter un produit
    elif choice_operation == "2":
        Ajouter_produit = input("Entrez le nom du produit que vous souhaitez ajouter : ")
        Ajouter_prix = float(input("Entrez le prix du produit que vous souhaitez ajouter : "))
        Ajouter_quantite = int(input("Entrez la quantité du produit que vous souhaitez ajouter : "))

        add_product(Ajouter_produit, Ajouter_prix, Ajouter_quantite)

    # supprimer un produit
    elif choice_operation == "3":
        delete_product = input("Entrez le nom du produit que vous souhaitez supprimer : ")
        remove_product(delete_product)
    
    # rechercher un produits
    elif choice_operation == "4":
        rechercher_produit = input("Entrez le nom du produit que vous recherchez : ")

        if is_product_available(rechercher_produit.lower()):
            if rechercher_produit.lower() in [product['name'] for product in products]:
                for product in products:
                    if product['name'] == rechercher_produit.lower():
                        print("")
                        print(f"== Le produit {rechercher_produit.upper()} est disponible ==")
                        # print(f"Prix : {product['price']} $")
                        # print(f"Quantité : {product['quantity']} en stock")
                        headers = {
                            "name": "Nom",
                            "price": "Prix ($)",
                            "quantity": "Quantité"
                        }
                        print(tabulate([product], headers=headers, tablefmt="grid"))
                        break
                    else:
                        print(f"Le produit {rechercher_produit} n'est pas disponible")
        else:
            print(f"Le produit {rechercher_produit} n'est pas disponible")
            
    # quitter le programme
    elif choice_operation == "5":
        print("Fin du programme")
        break