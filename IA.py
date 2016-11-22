#Crée un arbre de racine plateau et de fils les coups possibles en un coup
def coupsPossibles(plateau):
    coups = Arbre(plateau)
    for i in range (plateau.taille):
        for j in range(plateau.taille):
            if (plateau.mat[i,j] == 0):
                coups.ajout([i,j])
    return coups

#On garde deepCopy sous le coude au cas où, mais on en a plus besoin ici maintenant qu'on utilise les arbres
#def deepcopy(plateau):
#    plat = Plateau(plateau.taille)
#    for i in range(plateau.taille):
#        for j in range(plateau.taille):
#            plat.mat[i,j] = plateau.mat[i,j]
#    return plat

#Crée un arbre de racine plateau qui représente toutes les séries de nbEtage coups
def arbreCoups(plateau, nbEtage, joueur):
    abr = coupsPossibles(plateau)
    def aux(arbre, n, j):
        if (n == 0):
            return arbre
        else:
            for k in range(len(arbre.fils)):
                arbre.fils[k] = Arbre(arbre.fils[k])
                arbre.fils[k].fils = arbre.fils[:k] + arbre.fils[k+1:]
                aux(arbre.fils[k], n - 1, 3 - j)
            return arbre
    return aux(abr, nbEtage - 1, joueur)
#joueur n'a pour l'instant pas d'utilité ici
