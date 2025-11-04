import datetime
import json

class Produit:
    def __init__(self, id, prix, nom, stock):
        self.id = id
        self.prix = prix
        self.nom = nom
        self.stock = stock

    def retirer_du_stock(self, quantite):
        if quantite <= self.stock:
            self.stock -= quantite
            return True
        return False

class Panier:
    def __init__(self, date):
        self.date = date
        self.liste = []

    def ajouter(self, produit, quantite):
        self.liste.append((produit.nom, produit.prix, quantite))

    def retirer(self, index):
        if 0 <= index < len(self.liste):
            produit = self.liste.pop(index)
            print(f"{produit[0]} retiré du panier.")
        else:
            print("Index invalide.")

    def vider(self):
        self.liste = []

    def afficher(self):
        print("\n--- PANIER ---")
        print("Date :", self.date)
        if not self.liste:
            print("Panier vide.")
        else:
            total = 0
            for i, (nom, prix, quantite) in enumerate(self.liste):
                sous_total = prix * quantite
                print(f"{i+1}. {nom} - {prix} dh x {quantite} = {sous_total} dh")
                total += sous_total
            print("Montant total :", total, "dh")
        print("---------------------")

    def sauvegarder(self):
        data = {
            "date": self.date,
            "produits": [
                {"nom": nom, "prix": prix, "quantite": quantite}
                for (nom, prix, quantite) in self.liste
            ]
        }
        with open("panier.json", "w") as f:
            json.dump(data, f)
        print("Panier sauvegardé.")

    def restaurer(self):
        try:
            with open("panier.json", "r") as f:
                data = json.load(f)
                self.date = data["date"]
                self.liste = [(p["nom"], p["prix"], p["quantite"]) for p in data["produits"]]
            print("Panier restauré.")
        except FileNotFoundError:
            print("Aucune sauvegarde trouvée.")

stock = [
    Produit("P1", 150, "Clavier", 10),
    Produit("P2", 100, "Souris", 10),
    Produit("P3", 1200, "Écran", 10),
    Produit("P4", 300, "Casque", 10)
]

def afficher_stock():
    print("\n--- PRODUITS DISPONIBLES ---")
    for i, p in enumerate(stock):
        print(f"{i+1}. {p.nom} - {p.prix} dh (stock : {p.stock})")

def menu():
    date_achat = datetime.datetime.now().strftime("%d/%m/%Y")
    print("Date d'achat enregistrée :", date_achat)
    panier = Panier(date_achat)

    while True:
        print("\n--- MENU ---")
        print("1. Voir les produits")
        print("2. Ajouter au panier")
        print("3. Retirer du panier")
        print("4. Afficher le panier")
        print("5. Vider le panier")
        print("6. Sauvegarder le panier")
        print("7. Restaurer le panier")
        print("8. Quitter")

        choix = input("Votre choix : ")

        if choix == "1":
            afficher_stock()

        elif choix == "2":
            afficher_stock()
            i = int(input("Numéro du produit : ")) - 1
            if 0 <= i < len(stock):
                q = int(input("Quantité : "))
                produit = stock[i]
                if produit.retirer_du_stock(q):
                    panier.ajouter(produit, q)
                    print("Ajouté au panier.")
                else:
                    print("Stock insuffisant.")
            else:
                print("Numéro invalide.")

        elif choix == "3":
            panier.afficher()
            i = int(input("Numéro à retirer : ")) - 1
            panier.retirer(i)

        elif choix == "4":
            panier.afficher()

        elif choix == "5":
            panier.vider()
            print("Panier vidé.")

        elif choix == "6":
            panier.sauvegarder()

        elif choix == "7":
            panier.restaurer()

        elif choix == "8":
            print("Fin du programme.")
            break

        else:
            print("Choix invalide.")

menu()
