plateau = Plateau(9)
joueur = 1
pasDeGagnant = True

while(pasDeGagnant):
    marchePas = True
    while(marchePas):
        if joueur == 1:
            x = int(input("Xjoueur1 = "))
            y = int(input("Yjoueur1 = "))
        elif joueur == 2:
            x = int(input("Xjoueur2 = "))
            y = int(input("Yjoueur2 = "))
        marchePas = not(plateau.joue(joueur, x, y))
    pasDeGagnant = not(plateau.checkVictoire(joueur))
    if(pasDeGagnant):
        joueur = 3 - joueur
    plateau.affiche(1)
    
print("joueur n°" + str(joueur) + " gagne")
