from random import shuffle


class carte :
    def __init__(self, v, c):
        self.__valeur = v
        self.__couleur = c
    def nom_carte(self):
        print(self.__valeur, "de", self.__couleur)

class jeuCartes :
    def  __init__(self):
        couleur = ["pique","coeur","carreau","trefle"]
        valeur = ["As","2","3","4","5","6","7","8","9","10","valet","dame","roi"]
        self.__cartes = []
        for c in couleur:
            for v in valeur:
                self.__cartes.append(carte(v, c))
    def affichage(self):
        for c  in self.__cartes:
            c.nom_carte()
    def battre(self):
        shuffle(self.__cartes)
    def tirage(self):



jeu = jeuCartes()
print("======================")
print("affichage initial : ")
jeu.affichage()
jeu.battre()
print("======================")
print("affichage du jeu battue : ")
jeu.affichage()
