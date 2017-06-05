# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import pygame
from IA import *
from plateau import *
from classeArbre import *

plateau = Plateau(9, [], (-1,-1))
joueur = 1
pasDeGagnant = True

arbreGeneral1 = initialisation(plateau, 1)
arbreCoups1 = arbreGeneral1
cheminGeneral1 = []

arbreGeneral2 = initialisation(plateau, 2)
arbreCoups2 = arbreGeneral2
cheminGeneral2 = []


'''On laisse pour l'instant l'IA jouer en premier. Elle execute l'algorithme MCTS et joue le coup dans la racine de l'arbre renvoyé. 
On insere ensuite le plateau à la place de cette racine, pour de futures simulations'''
while(pasDeGagnant):
    caseOccupee = True
    while(caseOccupee):
        if joueur == 1:
            arbreCoups1 = mcts(arbreGeneral1, cheminGeneral1, arbreCoups1, plateau, 1)
            x = arbreCoups1.racine[0][0]
            y = arbreCoups1.racine[0][1]
        elif joueur == 2:
            arbreCoups2 = mcts(arbreGeneral2, cheminGeneral2, arbreCoups2, plateau, 2)
            x = arbreCoups2.racine[0][0]
            y = arbreCoups2.racine[0][1]
        caseOccupee = not(plateau.joue(joueur, (x, y)))
    pasDeGagnant = not(plateau.checkVictoire(joueur))
    if joueur == 2: #On actualise l'arbre de recherche de l'IA avec le coup de l'adversaire
        arbreCoups1 = rechercheCoup(arbreCoups1, plateau, cheminGeneral1, 1)
    if joueur == 1: #On actualise l'arbre de recherche de l'IA avec le coup de l'adversaire
        arbreCoups2 = rechercheCoup(arbreCoups2, plateau, cheminGeneral2, 2)
    if(pasDeGagnant):
        joueur = 3 - joueur
    plateau.affiche2()

pygame.quit()  
print("joueur n°" + str(joueur) + " gagne")