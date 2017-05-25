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
arbreGeneral = initialisation(plateau)
arbreCoups = arbreGeneral
cheminGeneral = []

isThinking=True
canThink=True
updateArbre=False
x=0
y=0



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
        global arbreGeneral
        global cheminGeneral
        global updateArbre
        while pasDeGagnant :
            if(joueur==1 and canThink):
                print("joueur",joueur)
                #print("avant",arbreCoups.nbTot(0))
                isThinking=True
                arbreCoups,coupSelect = mctsThread(arbreGeneral, cheminGeneral,arbreCoups, plateau,True)
                x = arbreCoups.fils[coupSelect].racine[0][0]
                y = arbreCoups.fils[coupSelect].racine[0][1]
                isThinking=False
                canThink=False
                #print("apres",arbreCoups.nbTot(0))
                print("fin joueur",joueur)
            else:
                while joueur==2 :
                    if(not(updateArbre)):
                        arbreCoups=mctsThread(arbreGeneral, cheminGeneral,arbreCoups, plateau,False)





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




thread= ThreadIA()
thread.start()
'''On laisse pour l'instant l'IA jouer en premier. Elle execute l'algorithme MCTS et joue le coup dans la racine de l'arbre renvoyé. 
On insere ensuite le plateau à la place de cette racine, pour de futures simulations'''
while(pasDeGagnant):
    caseOccupee = True
    while(caseOccupee):
        if joueur == 1:
            canThink=True
            while isThinking:
                1
            #arbreCoups = mcts(arbreGeneral, cheminGeneral, arbreCoups, plateau)
            #x = arbreCoups.racine[0][0]
            #y = arbreCoups.racine[0][1]
        elif joueur == 2:
            x = int(input("Xjoueur2 = "))
            y = int(input("Yjoueur2 = "))
        caseOccupee = not(plateau.joue(joueur, (x, y)))
    pasDeGagnant = not(plateau.checkVictoire(joueur))
    if joueur == 2: #On actualise l'arbre de recherche de l'IA avec le coup de l'adversaire
        updateArbre=True
        arbreCoups = rechercheCoup(arbreCoups, plateau, cheminGeneral)
        updateArbre=False
    if(pasDeGagnant):
        joueur = 3 - joueur
    plateau.affiche2()

pygame.quit()  
print("joueur n°" + str(joueur) + " gagne")