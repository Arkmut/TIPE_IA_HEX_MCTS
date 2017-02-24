#import matplotlib.pyplot as plt

class Plateau:
    # une case est vide (=0) joueur 1 (=1) et joueur 2 (=2)
    mat = []
    taille = 0

    def __init__(self, largeur):
        self.taille = largeur
        self.mat = [[]] * self.taille
        for i in range(self.taille):
            self.mat[i] = [0] * self.taille
        
    
    def joue(self, joueur, i, j):
        if(self.mat[i][j] == 0):
            self.mat[i][j] = joueur
            return True
        else:
            return False

    def affiche(self, nAffichage = 1):
        if(nAffichage == 1):
            s = ""
            for i in range(0, self.taille):
                s += str(i) + "  "
            print("  " * self.taille + "x\y", s)
            for i in range(0, self.taille):
                print("  " * (self.taille - i - 1), i, self.mat[i])
        # elif(nAffichage == 2):
        #     xx = np.linspace(0,self.taille, self.taille)
        #     yy = np.linspace(0,self.taille, self.taille)
        #     #plt.pcolormesh(xx,yy,self.taille, shading='flat')
        #     plt.imshow(self.mat)
        #     plt.axis('image')
        #     plt.draw()
        #     #plt.show()
    
    def chemin(self, joueur, xDepart, yDepart, dejaVu):
        dejaVu.append((xDepart, yDepart))
        #Cas de base, on est arrivé de l'autre coté du plateau
        if((yDepart == self.taille-1 and joueur == 1) or (xDepart == self.taille-1 and joueur == 2)):
            return True
        else:
            #On créé la liste des cases adjacentes
            ptsAdja = []
            if(xDepart < self.taille-1):
                ptsAdja.append((xDepart+1, yDepart))
                if(yDepart < self.taille-1):
                    ptsAdja.append((xDepart+1, yDepart+1))
            if(xDepart > 0):
                ptsAdja.append((xDepart-1, yDepart))
                if(yDepart > 0):
                    ptsAdja.append((xDepart-1, yDepart-1))
            if(yDepart < self.taille-1):
                ptsAdja.append((xDepart, yDepart+1))
            if(yDepart > 0):
                ptsAdja.append((xDepart, yDepart-1))
            #On retire à cette liste les cases déjà visitées
            i = 0 
            while(i < len(ptsAdja)):
                for j in range(0, len(dejaVu)):
                    if(dejaVu[j] == ptsAdja[i]):
                        ptsAdja.remove(ptsAdja[i])
                        i -= 1
                        break
                i += 1
            #On applique récursivement chemin à chaque case de la liste contenant un pion de joueur
            for i in range(0, len(ptsAdja)):
                if((self.mat[ptsAdja[i][0]][ptsAdja[i][1]] == joueur) and (self.chemin(joueur, ptsAdja[i][0], ptsAdja[i][1], dejaVu))):
                    return True
            return False
        
    def checkVictoire(self, joueur):
        sortie = False
        if(joueur == 1):
            for i in range(0, self.taille):
                if(self.mat[i][0] == joueur) and not(sortie):
                    sortie = self.chemin(joueur, i, 0, [])
        if(joueur == 2):
            for i in range(0, self.taille):
                if(self.mat[0][i] == joueur) and not(sortie):
                    sortie = self.chemin(joueur, 0, i, [])
        return sortie

##Boucle de jeu

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
    marchePas = True
    x = -1
    y = -1
    while(marchePas):
        if joueur == 1:
            arbreCoups = mcts(arbreCoups)
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
