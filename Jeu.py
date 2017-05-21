# -*- coding: utf-8 -*-
import pygame 
import time
from Plateau import *
from IA import *
from ClasseArbre import *

from threading import Thread

plateau = Plateau(9, [], (-1,-1))
joueur = 1
pasDeGagnant = True
arbreCoups = initialisation(plateau)
isThinking=True
canThink=True
updateArbre=False
x=0
y=0
testValue=-1


class ThreadPygame(Thread):
    def __init__(self):
        global plateau
        ''' Constructor. '''
        Thread.__init__(self)
        print("affichage init")
    
    def run(self):
        global plateau
        global pasDeGagnant
        while pasDeGagnant:
            plateau.affiche2()
            time.sleep(0.1)







class ThreadIA(Thread):
    def __init__(self):
        ''' Constructor. '''
        Thread.__init__(self)
    
    def run(self):
        global pasDeGagnant
        global joueur
        global isThinking
        global canThink
        global x
        global y
        global arbreCoups
        global updateArbre
        global testValue
        while pasDeGagnant :
            if(joueur==1 and canThink):
                print("joueur",joueur)
                #print("avant",arbreCoups.nbTot(0))
                isThinking=True
                arbreCoups,coupSelect = mctsThread(arbreCoups, plateau,True)
                x = arbreCoups.fils[coupSelect].racine[0][0]
                y = arbreCoups.fils[coupSelect].racine[0][1]
                isThinking=False
                canThink=False
                #print("apres",arbreCoups.nbTot(0))
                print("fin joueur",joueur)
            else:
                while joueur==2 and not(updateArbre):
                    arbreCoups=mctsThread(arbreCoups, plateau,False)
















thread= ThreadIA()
thread.start()
threadPlateau=ThreadPygame()
#threadPlateau.start()
# while(pasDeGagnant):
#     marchePas = True
#     while(marchePas):
#         if joueur == 1:
#             x = int(input("Xjoueur1 = "))
#             y = int(input("Yjoueur1 = "))
#         elif joueur == 2:
#             x = int(input("Xjoueur2 = "))
#             y = int(input("Yjoueur2 = "))
#         marchePas = not(plateau.joue(joueur, (x, y)))
#     pasDeGagnant = not(plateau.checkVictoire(joueur))
#     if(pasDeGagnant):
#         joueur = 3 - joueur
#     plateau.affiche(1)

'''On laisse pour l'instant l'IA jouer en premier. Elle execute l'algorithme MCTS et joue le coup dans la racine de l'arbre renvoyé. 
On insere ensuite le plateau à la place de cette racine, pour de futures simulations'''
while(pasDeGagnant):
    caseOccupee = True
    while(caseOccupee):
        if joueur == 1:
            canThink=True
            #arbreCoups = mcts(arbreCoups, plateau)
            #x = arbreCoups.racine[0][0]
            #y = arbreCoups.racine[0][1]
            while isThinking:
                1
        elif joueur == 2:
            x = int(input("Xjoueur2 = "))
            y = int(input("Yjoueur2 = "))
        caseOccupee = not(plateau.joue(joueur, (x, y)))
    pasDeGagnant = not(plateau.checkVictoire(joueur))
    if joueur == 2: #On actualise l'arbre de recherche de l'IA avec le coup de l'adversaire
        updateArbre=True
        arbreCoups = rechercheCoup(arbreCoups, plateau)
        updateArbre=False
    if(pasDeGagnant):
        joueur = 3 - joueur
    plateau.affiche2()

pygame.quit()  
print("joueur n°" + str(joueur) + " gagne")






               
           