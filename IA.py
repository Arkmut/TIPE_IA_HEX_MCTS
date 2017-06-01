# -*- coding: utf-8 -*-
import random as rd
import time
from classeArbre import *
from plateau import *
from math import sqrt, log

'''
Ici sont utilisé la structure de plateau et la structure d'arbre.
Cette dernière est utilisée afin de représenter l'arbre des coups explorés par MCTS.
Elle s'agence de la manière suivante:
    - arbre.racine contient une liste de deux éléments, respectivement:
        - un tuple de coordonées (i, j) représentant un coup. S'il sagit du sommet global de l'arbre, c'est le coup venant d'être joué
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
'''


## Fonctions diverses

#Crée un arbre de racine plateau et de fils les coups possibles en un coup
def coupsPossibles(plateau):
    coups = Arbre(plateau.coup)
    for i in range (plateau.taille):
        for j in range(plateau.taille):
            if (plateau.mat[i][j] == 0):
                coups.ajout(Arbre((i, j)))
    return coups

#Joue une partie aléatoire à partir d'un état du plateau et renvoie le joueur gagnant
def partieAleat(plateau, joueur):
    plat = plateau.deepcopy()
    coups = coupsPossibles(plat).fils
    j = joueur
    while coups != []:
        coupReac = reaction(plat, j)
        if coupReac != plat.coup:
            k = 0
            while coups[k].racine != coupReac: k += 1
            coups.pop(k)
            plat.joue(j, coupReac)
        else:
            k = rd.randint(0, len(coups) - 1)
            plat.joue(j, coups.pop(k).racine)
        j = 3 - j
    if plat.checkVictoire(1):
        return 1
    else:
        return 2

#Ajoute au noeuds un couple pour la notation
def transfoArbre(arbre):
    arbre.racine = [arbre.racine, [0, 0]]
    if arbre.fils != []:
        for elt in arbre.fils:
            transfoArbre(elt)

def initialisation(plateau):
    coupReac = reaction(plateau, 1)
    if plateau.coup != coupReac:
        arbre = Arbre(plateau.coup)
        arbre.ajout(Arbre(coupReac))
        transfoArbre(arbre)
    else:
        arbre = coupsPossibles(plateau)
        transfoArbre(arbre)
    return arbre

def rechercheCoup(arbre, plateau, cheminGeneral):
    for k in range(len(arbre.fils)):
        if plateau.coup == arbre.fils[k].racine[0]:
            cheminGeneral.append(k)
            return arbre.fils[k]
    print("fail")
    arbre.ajout(initialisation(plateau))
    leng = len(arbre.fils)
    return arbre.fils[leng-1]
    #quand le joueur joue un coup non présent dans l'arbre, n'est pas sensé arriver

##MCTS
''' MCTS repose sur quatre étapes :
    - Sélection: on sélectionne le coup le plus prometteur à partir d'un arbre de notation de coups. 
        Cette sélection repose sur des notation antérieures des coups.
    - Expansion: on ajoute à ce coup «père» tout ses coups «fils» dans l'arbre, c'est à dire 
        les coups possible après le coup sélectionné.
    - Simulation : pour chacun des coups fils nouvellement rajoutés, on simule une partie aléatoire, 
        et on note le coup fils avec le résultat de cette partie.
    - Rétro-propagation (Ici backtracking): On actualise les notations des nœuds parents avec le résultat de cette partie.'''
#Coeur de l'algorithme
def mcts(arbreGeneral, cheminGeneral, arbre, plateau):
    t0 = time.time()
    t1 = t0
    while t1 < t0 + 10:
        p_copy = plateau.deepcopy()
        select, chemin, joueur = selexpansion(arbre, p_copy, [], 1) #/!\ Modifie l'état du plateau p_copy
        simulation(select, p_copy, joueur, 1)
        backtracking(arbreGeneral, cheminGeneral + chemin)
        t1 = time.time()
    coupSelect = minimise(arbre)
    cheminGeneral.append(coupSelect)
    #arbreGeneral.affiche()
    return arbre.fils[coupSelect]
    
# Maximise et minimise sont des fonctions utilisées pour la sélection

def minimise(arbre): #si le joueur doit jouer
    x = arbre.racine[1][1]
    #print("min", x)
    noteMin = (arbre.fils[0].racine[1][0]/arbre.fils[0].racine[1][1]) + 0.3*sqrt(2*log(x)/arbre.fils[0].racine[1][1])
    rangMin = 0
    leng = len(arbre.fils) #nombre de fils
    for k in range(1, leng):
        xk = arbre.fils[k].racine[1][0] #nb de parties gagnées par le fils k
        yk = arbre.fils[k].racine[1][1] #nb de partie jouées depuis le fils k
        note = xk/yk + 0.3*sqrt(log(x)/yk) #fonction de notation
        if note < noteMin: # on essaie de minimiser la note
            noteMin = note
            rangMin = k
    return rangMin

def maximise(arbre): #Si l'IA doit jouer
    x = arbre.racine[1][1]+1
    #print("max", x)
    print("x",x)
    print(2*log(x)/arbre.fils[0].racine[1][1])
    noteMax = (arbre.fils[0].racine[1][0]/arbre.fils[0].racine[1][1]) + 0.3*sqrt(2*log(x)/arbre.fils[0].racine[1][1])
    rangMax = 0
    leng = len(arbre.fils) #nombre de fils
    for k in range(1, leng):
        xk = arbre.fils[k].racine[1][0] #nb de parties gagnées par le fils k
        yk = arbre.fils[k].racine[1][1] #nb de partie jouées depuis le fils k
        note = xk/yk + 0.3*sqrt(log(x)/yk) #fonction de notation 
        if note > noteMax: # on essaie de maximiser la note
            noteMax = note
            rangMax = k
    return rangMax

#renvoie l'arbre du coup sélectionné et le chemin pour parvenir à ce coup
def selexpansion(arbre, plateau, chemin, joueur):
    if arbre.fils == []:
        if joueur == 1:
            coupReac = reaction(plateau, 1)
            if coupReac != plateau.coup:
                arbre.ajout(Arbre([coupReac, [0, 0]]))
            else:
                coups = coupsPossibles(plateau)
                transfoArbre(coups)
                arbre.fils = coups.fils   
        else:
            coups = coupsPossibles(plateau)
            transfoArbre(coups)
            arbre.fils = coups.fils
        k = rd.randint(0, len(arbre.fils) - 1)
        chemin.append(k)
        plateau.joue(joueur, arbre.fils[k].racine[0])
        return arbre.fils[k], chemin, (3 - joueur)
    else:
        coupsNonNotes = []
        for k in range(len(arbre.fils)):
            if arbre.fils[k].racine[1][1] == 0: coupsNonNotes.append(k) 
        if coupsNonNotes != []:
            k = rd.randint(0, len(coupsNonNotes) - 1)
            chemin.append(k)
            plateau.joue(joueur, arbre.fils[coupsNonNotes[k]].racine[0])
            return arbre.fils[coupsNonNotes[k]], chemin, (3 - joueur)
        else:
            #L'IA essaie de jouer les meilleurs coups pour elle, et le joueur les plus mauvais coups pour l'IA
            if joueur == 1:
                coupSelect = maximise(arbre)
            else:
                coupSelect = minimise(arbre)
            chemin.append(coupSelect) # chemin est une liste d'int. 
            #Chaque int indique une place de la liste arbre.fils et donc le coup suivant
            plateau.joue(joueur, arbre.fils[coupSelect].racine[0])
            return selexpansion(arbre.fils[coupSelect], plateau, chemin, 3 - joueur) 
        
        
    
def simulation(arbre, plateau, joueur, n): #n le nb de parties simulées
    for _ in range(n):
        x = partieAleat(plateau, joueur) # x = 1 ou 2 selon qui gagne
        arbre.racine[1][1] += 1 #on rajoute une visite  
        if x == 1:
            arbre.racine[1][0] += 1 #on rajoute une victoire

def backtracking(arbre, chemin):
    if chemin == []:
        ajout_gain = arbre.racine[1][0]
        ajout_jouees = arbre.racine[1][1]
        return ajout_gain, ajout_jouees
    else:
        ajout_gain, ajout_jouees = backtracking(arbre.fils[chemin[0]], chemin[1:])
        arbre.racine[1][0] += ajout_gain
        arbre.racine[1][1] += ajout_jouees
        return ajout_gain, ajout_jouees

def reaction(plateau, joueur):
    j = joueur
    (x, y) = plateau.coup
    if (x, y) == (-1, -1):
        return (x, y)
    leng = plateau.taille
    vois = [-1] * 6
    if  x > 0:
        if x < leng - 1:
            if y > 0:
                if y < leng - 1:
                    vois[0] = plateau.mat[x-1][y-1]
                    vois[1] = plateau.mat[x-1][y]
                    vois[2] = plateau.mat[x][y+1]
                    vois[3] = plateau.mat[x+1][y+1]
                    vois[4] = plateau.mat[x+1][y]
                    vois[5] = plateau.mat[x][y-1]
                else:
                    vois[0] = plateau.mat[x-1][y-1]
                    vois[1] = plateau.mat[x-1][y]
                    vois[4] = plateau.mat[x+1][y]
                    vois[5] = plateau.mat[x][y-1]
            else:
                vois[1] = plateau.mat[x-1][y]
                vois[2] = plateau.mat[x][y+1]
                vois[3] = plateau.mat[x+1][y+1]
                vois[4] = plateau.mat[x+1][y]
        else:
            if y > 0:
                if y < leng - 1:
                    vois[0] = plateau.mat[x-1][y-1]
                    vois[1] = plateau.mat[x-1][y]
                    vois[2] = plateau.mat[x][y+1]
                    vois[5] = plateau.mat[x][y-1]
                else:
                    vois[0] = plateau.mat[x-1][y-1]
                    vois[1] = plateau.mat[x-1][y]
                    vois[5] = plateau.mat[x][y-1]
            else:
                vois[1] = plateau.mat[x-1][y]
                vois[2] = plateau.mat[x][y+1]
    else:
        if y > 0:
            if y < leng - 1:
                vois[2] = plateau.mat[x][y+1]
                vois[3] = plateau.mat[x+1][y+1]
                vois[4] = plateau.mat[x+1][y]
                vois[5] = plateau.mat[x][y-1]
            else:
                vois[4] = plateau.mat[x+1][y]
                vois[5] = plateau.mat[x][y-1]
        else:
            vois[2] = plateau.mat[x][y+1]
            vois[3] = plateau.mat[x+1][y+1]
            vois[4] = plateau.mat[x+1][y]
    if j == 1 and y == 0:
        if vois[2] == j and vois[1] == 0: return (x-1, y)
        if vois[3] == j and vois[4] == 0: return (x+1, y)
    if j == 1 and y == leng-1:
        if vois[0] == j and vois[1] == 0: return (x-1, y)
        if vois[5] == j and vois[4] == 0: return (x+1, y)
    if j == 2 and x == 0:
        if vois[4] == j and vois[5] == 0: return (x, y-1)
        if vois[3] == j and vois[2] == 0: return (x, y+1)
    if j == 2 and x == leng-1:
        if vois[0] == j and vois[5] == 0: return (x, y-1)
        if vois[1] == j and vois[2] == 0: return (x, y+1) 
    if vois[4] == 0 and vois[5] == j and vois[3] == j:
        return (x+1, y)
    if vois[1] == 0 and vois[0] == j and vois[2] == j:
        return (x-1, y)
    if vois[3] == 0 and vois[4] == j and vois[2] == j:
        return (x+1, y+1)
    if vois[0] == 0 and vois[5] == j and vois[1] == j:
        return (x-1, y-1)
    if vois[5] == 0 and vois[0] == j and vois[4] == j:
        return (x, y-1)
    if vois[2] == 0 and vois[1] == j and vois[3] == j:
        return (x, y+1)
    return(x, y)