import random as rd

'''
Ici sont utilisé la structure de plateau et la structure d'arbre.
Cette dernière est utilisée afin de représenter l'arbre des coups explorés par MCTS.
Elle s'agence de la manière suivante:
    - arbre.racine contient une liste de deux éléments, respectivement:
        - un couple de coordonées [i, j] représentant un coup
            OU , s'il sagit du sommet global de l'arbre, du plateau
        - un couple de notation [x, y] avec:
            - x le nombre de parties gagnées en jouant ce coup
            - y le nombre de fois que ce coup a été exploré
    - arbre.fils est la liste des arbres représentant les coups explorés ultérieurs au coup de la racine.
    
A la fin de chaque tour de boucle de la fonction mcts, l'arbre des coups doit respecter les propriétés suivantes:
    -l'arbre est du type décrit ci-dessus
    -les fils d'un arbre ne peuvent être que des arbres
    -un coup n'est pas présent dans sa propre descendance
    -le nombre de parties gagné d'un coup est la somme du nombre de parties gagnées des coups fils
    -le nombre de fois qu'un coup a été exploré est la somme du nombre de fois que les coups fils ont été exploré
    -tout coup a été noté au moins une fois
'''


## Fonctions diverses

#Crée un arbre de racine plateau et de fils les coups possibles en un coup
def coupsPossibles(plateau):
    coups = Arbre(plateau)
    for i in range (plateau.taille):
        for j in range(plateau.taille):
            if (plateau.mat[i][j] == 0):
                coups.ajout(Arbre([i, j]))
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

#Effectue une copie en mémoire du plateau
def deepcopy(plateau):
   plat = Plateau(plateau.taille)
   for i in range(plateau.taille):
       for j in range(plateau.taille):
           plat.mat[i][j] = plateau.mat[i][j]
   return plat

#Joue une partie aléatoire à partir d'un état du plateau et renvoie le joueur gagnant
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

def parcoursProfondeur(arbre):
    #action sur racine
    if arbre.fils != []:
        for elt in arbre.fils:
            parcoursProfondeur(elt)

#Ajoute au noeuds un couple pour la notation
def transfoArbre(arbre):
    arbre.racine = [arbre.racine, [0, 0]]
    if arbre.fils != []:
        for elt in arbre.fils:
            transfoArbre(elt)

##MCTS

#Coeur de l'algorithme
def mcts(arbre):
    for _ in range(1000):
        p_copy = deepcopy(arbre.racine)
        #SELECTION d'un coup à explorer
        select, chemin = selection(arbre, p_copy)  #/!\ Modifie l'état du plateau
        #EXPANSION : on ajoute à l'arbre des coups les coups ultérieurs au coup sélectionné 
        expansion(select, p_copy)
        #SIMULATION de parties purement aléatoire pour les coups nouvellement rajoutés à l'arbre
        gagnees, jouees = simulation(select, p_copy) 
        #RETROPROPAGATION: on actualise les notes des coups antérieurs avec les coups fraîchements notés
        backtracking(arbre, chemin, gagnee, jouees)
    noteMax, rangMax = minimise(arbre.fils)
    selected = arbre.fils[k]
    
#renvoie la note et le rang du fils de meilleure notation
def minimise(listeFils):
    noteMax = 0
    rangMax = 0
    l = len(listeFils) #nombre de fils
    for k in range(l):
        x = listeFils[k].racine[1][0] #nb de parties gagnées par le fils k
        y = listeFils[k].racine[1][1] #nb de partie jouées depuis le fils k
        note = y - x #fonction de notation
        if note < noteMax:
            noteMax = note
            rangMax = k
    return noteMax, rangMax

#renvoie l'arbre du coup sélectionné et le chemin pour parvenir à ce coup
def selection(arbre, plateau, chemin = []): 
    if arbre.fils = []:
        return arbre, chemin
    else:
        #n = arbre.racine[1][1] #nombre de parties jouées depuis cette racine
        noteMax, rangMax = minimise(arbre.fils)
        chemin.append(rangMax) # chemin est une liste d'int. 
        #Chaque int indique une place de la liste arbre.fils et donc le coup suivant
        plateau.joue(1, arbre.fils[rangMax].racine[0][0], arbre.fils[rangMax].racine[0][1])
        return selection(arbre.fils[rangMax], chemin)

def expansion(arbre, plateau):
    coups = coupsPossibles(plateau)
    transfoArbre(coups)
    arbre.fils = coups.fils
    
def simulation(arbre, plateau, n = 1): #n le nb de parties simulées par fils créé
    gagnees = 0 # nombre de parties gagnées lors de la simulation
    jouees = 0 # nombre de parties jouées lors de la simulation
    for fils in arbre.fils:
        plateau.joue(1, fils.racine[0][0], fils.racine[0][1]) # on joue le coup fils sélectionné
        for _ in range(n):
            x = partieAleat(plateau, 2)# x = 1 ou 2 selon qui gagne
            fils.racine[1][1] += 1 #on rajoute une visite au fils  
            jouees += 1 
            if x == 1:
                fils.racine[1][0] += 1 #on rajoute une victoire
                gagnee += 1  
        plateau.joue(0, fils.racine[0][0], fils.racine[0][1]) # on retire le coup qu'on a joué avant la boucle for
    return gagnees, jouees

def backtracking(arbre, chemin, gagnees, jouees):
    if chemin == []:
        ajout_gain = gagnees - arbre.racine[1][0]
        ajout_jouees = jouees - arbre.racine[1][1]
        arbre.racine[1][0] = gagnees
        arbre.racine[1][1] = jouees
        return ajout_gain, ajout_jouees
    else:
        ajout_gain, ajout_jouees = backtracking(arbre.fils[chemin[0]], chemin[1:], gagnees, jouees)
        arbre.racine[1][0] += ajout_gain
        arbre.racine[1][1] += ajout_jouees
        return ajout_gain, ajout_jouees

    
