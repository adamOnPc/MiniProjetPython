class domino :
    def __init__(self,v1 ,v2):
        self.__valeur1 = v1
        self.__valeur2 = v2

    def affichage(self):
        print(str(self.__valeur1) + " / " + str(self.__valeur2))
    def affichageV2(self):
        return self.__valeur1 + self.__valeur2

print("------------------------------------------------")
print("domino 5, 6 :")
d = domino(5, 6)
d.affichage()
print("------------------------------------------------")
print("domino : 1, 2 :")
d1 = domino(1,2)
print(d1.affichageV2())

listeDomoinos = []
for i in range(7):
    listeDomoinos.append(domino(6,1))
somme = 0
for i in range(len(listeDomoinos)):