listA = [1, 2, 3, 4, 5, 6]
joueur1 = input("nom joueur 1 :")
joueur2 = input("nom joueur 2 :")
listJ = [joueur1, joueur2]
rotation = 0

while sum(listA) > 0 :
    print(listA)
    print("joueur :", listJ[rotation])
    tas = eval(input("quel tas tu choisie :")) -1
    nombreA = eval(input("quel est le nombre d'alumette que tu choisie :"))
    if 0 <= tas < len(listA) and 0 < nombreA <= listA[tas] :
        listA[tas] -= nombreA
        rotation = 1 - rotation
    else: print("le nombre tapper n'est pas présent dans la list :")
if sum(listA) == 0 :
        print("Le Joueur Gagnant est :", listJ[rotation])
