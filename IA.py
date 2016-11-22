import random as rd

#Crée un arbre de racine plateau et de fils les coups possibles en un coup
def coupsPossibles(plateau):
    coups = Arbre(plateau)
    for i in range (plateau.taille):
        for j in range(plateau.taille):
            if (plateau.mat[i,j] == 0):
                coups.ajout(Arbre([i,j]))
    return coups

#Crée un arbre de racine plateau qui représente toutes les séries de nbEtage coups
def arbreCoups(plateau, nbEtage, joueur):
    abr = coupsPossibles(plateau)
    def aux(arbre, n, j):
        if (n == 0):
            return arbre
        else:
            for k in range(len(arbre.fils)):
                arbre.fils[k].fils = [Arbre(arbre.fils[i].racine) for i in range(len(arbre.fils)) if i != k]
                aux(arbre.fils[k], n - 1, 3 - j)
            return arbre
    return aux(abr, nbEtage - 1, joueur)
#joueur n'a pour l'instant pas d'utilité ici

def afficheArbre(arbre, nEtage = 0):
    if arbre.fils == []:
        print("   " * nEtage, arbre.racine)
    else:
        print("   " * nEtage, arbre.racine)
        for elt in arbre.fils:
            afficheArbre(elt, nEtage + 1)

def deepcopy(plateau):
   plat = Plateau(plateau.taille)
   for i in range(plateau.taille):
       for j in range(plateau.taille):
           plat.mat[i,j] = plateau.mat[i,j]
   return plat

def partieAleat(plateau, joueur):
    plat = deepcopy(plateau)
    coups = coupsPossibles(plat).fils
    coupsJoues = []
    while coups != []:
        k = rd.randint(0, len(coups) - 1)
        coupsJoues.append(coups.pop(k).racine)
    for k in coupsJoues:
        plateau.joue(joueur, k[0], k[1])
        joueur = 3 - joueur
    if plateau.checkVictoire(1):
        return 1
    else:
        return 2
