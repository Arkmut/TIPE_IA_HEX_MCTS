plateau = Plateau(5)
joueur = 1
pasDeGagnant = True
arbreCoups = initialisation(plateau)

# while(pasDeGagnant):
#     marchePas = True
#     while(marchePas):
#         if joueur == 1:
#             x = int(input("Xjoueur1 = "))
#             y = int(input("Yjoueur1 = "))
#         elif joueur == 2:
#             x = int(input("Xjoueur2 = "))
#             y = int(input("Yjoueur2 = "))
#         marchePas = not(plateau.joue(joueur, x, y))
#     pasDeGagnant = not(plateau.checkVictoire(joueur))
#     if(pasDeGagnant):
#         joueur = 3 - joueur
#     plateau.affiche(1)

while(pasDeGagnant):
    CaseOccupée = True
    x = -1
    y = -1
    while(marchePas):
'''On laisse pour l'instant l'IA jouer en premier. Elle execute l'algorithme MCTS et joue les coups dans la racine de l'arbre renvoyé. On insere ensuite le plateau à la place de cette racine, pour de futures simulations'''
        if joueur == 1:
            arbreCoups = mcts(arbreCoups)
            x = arbreCoups.racine[0][0]
            y = arbreCoups.racine[0][1]
            arbreCoups.racine[0] = plateau
        elif joueur == 2:
            x = int(input("Xjoueur2 = "))
            y = int(input("Yjoueur2 = "))
        CaseOccupée = not(plateau.joue(joueur, x, y))
    pasDeGagnant = not(plateau.checkVictoire(joueur))
    if joueur == 2: #On actualise l'arbre de recherche de l'IA avec le coup de l'adversaire
        arbreCoups = rechercheCoup(arbreCoups, x, y, plateau)
    if(pasDeGagnant):
        joueur = 3 - joueur
    plateau.affiche(1)
    
print("joueur n°" + str(joueur) + " gagne")
