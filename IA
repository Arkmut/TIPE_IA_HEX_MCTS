def coupsPossibles(plateau):
    coups = []
    for i in range (plateau.taille):
        for j in range(plateau.taille):
            if (plateau.mat[i,j] == 0):
                coups.append([i,j])
    return coups

def deepcopy(plateau):
    plat = Plateau(plateau.taille)
    for i in range(plateau.taille):
        for j in range(plateau.taille):
            plat.mat[i,j] = plateau.mat[i,j]
    return plat

def feuille(plateau, nbEtage, joueur):
    if (nbEtage == 1):
        l = coupsPossibles(plateau)
        coups = []
        for k in l:
            coups.append([k])
        return coups
    else:
        l = coupsPossibles(plateau)
        coups = []
        for k in l:
            plat = deepcopy(plateau)
            plat.mat[k[0], k[1]] = joueur
            coupsK = feuille(plat, nbEtage - 1, 3 - joueur)
            for m in coupsK:
                m.insert(0, k) 
            coups.extend(coupsK)
        return coups
