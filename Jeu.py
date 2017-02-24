
plateau = Plateau(5)
joueur = 1
pasDeGagnant = True
arbreCoups = initialisation(plateau)

#while(pasDeGagnant):
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
    marchePas = True
    x = -1
    y = -1
    while(marchePas):
        if joueur == 1:
            arbreCoups.affiche(0)
            arbreCoups = mcts(arbreCoups)
            print("arbre final \n")
            arbreCoups.afficheRacine()
            x = arbreCoups.racine[0][0]
            y = arbreCoups.racine[0][1]
            arbreCoups.racine[0] = plateau
        elif joueur == 2:
            x = int(input("Xjoueur2 = "))
            y = int(input("Yjoueur2 = "))
        marchePas = not(plateau.joue(joueur, x, y))
    pasDeGagnant = not(plateau.checkVictoire(joueur))
    if joueur == 2:
        arbreCoups = rechercheCoup(arbreCoups, x, y, plateau)
    if(pasDeGagnant):
        joueur = 3 - joueur
    plateau.affiche(1)
    
print("joueur n°" + str(joueur) + " gagne")
