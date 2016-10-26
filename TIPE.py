import numpy as np
import matplotlib.pyplot as plt
class Plateau:
    # une case est vide (=0) joueur 1 (=1) et joueur 2 (=2)
    mat = []
    taille = 0
    def __init__(self, largeur):
        self.taille = largeur
        self.mat = np.zeros((self.taille, self.taille))
    
    def joue(self,joueur, i,j):
        if(self.mat[i,j] == 0):
            self.mat[i,j] = joueur
            return True
        else:
            return False

    def affiche(self, texte):
        if(texte):
            l = []
            s = ""
            for i in range(0, self.taille):
                l.append(i)
                s += str(i)+"   "
            print("x\y", s)
            for i in range(0, len(l)):
                print(l[i], self.mat[i])
        else:
            xx = np.linspace(0,self.taille, self.taille)
            yy = np.linspace(0,self.taille, self.taille)
            #plt.pcolormesh(xx,yy,self.taille, shading='flat')
            plt.imshow(self.mat)
            plt.axis('image')
            plt.draw()
            #plt.show()
    
    def chemin(self, joueur, xDepart, yDepart, pileDejaParcouru):
        pileDejaParcouru.append((xDepart, yDepart))
        if((yDepart == self.taille-1 and joueur == 1) or (xDepart == self.taille-1 and joueur == 2)):
            return True
        else:
            ptsAdjacents = []
            if(xDepart < self.taille-1):
                ptsAdjacents.append((xDepart+1, yDepart))
                if(yDepart < self.taille-1):
                    ptsAdjacents.append((xDepart+1, yDepart+1))
            if(xDepart > 0):
                ptsAdjacents.append((xDepart-1,yDepart))
                if(yDepart > 0):
                    ptsAdjacents.append((xDepart-1, yDepart-1))
            if(yDepart < self.taille-1):
                ptsAdjacents.append((xDepart, yDepart+1))
            if(yDepart > 0):
                ptsAdjacents.append((xDepart, yDepart-1))
            i = 0
            while(i < len(ptsAdjacents)):
                for j in range(0, len(pileDejaParcouru)):
                    if(pileDejaParcouru[j] == ptsAdjacents[i]):
                        ptsAdjacents.remove(ptsAdjacents[i])
                        i -= 1
                i += 1
            for i in range(0,len(ptsAdjacents)):
                if(self.mat[ptsAdjacents[i][0], ptsAdjacents[i][1]]==joueur):
                    if(self.chemin(joueur, ptsAdjacents[i][0], ptsAdjacents[i][1],pileDejaParcouru)):
                        return True
            return False
        
    def checkVictoire(self, joueur):
        sortie = False
        if(joueur == 1):
            for i in range(0, self.taille):
                if(self.mat[i,0] == joueur):
                    if(not(sortie)):
                        sortie = self.chemin(joueur, i, 0, [])
        if(joueur == 2):
            for i in range(0, self.taille):
                if(self.mat[0,i] == joueur):
                    if(not(sortie)):
                        sortie = self.chemin(joueur, 0, i, [])
        return sortie

plateau = Plateau(9)
joueur = 1
pasDeGagnant = True
plt.show()
while(pasDeGagnant):
    marchePas = True
    while(marchePas):
        if joueur == 1:
            x = input("Xjoueur1 = ")
            y = input("Yjoueur1 = ")
        elif joueur == 2:
            x = input("Xjoueur2 = ")
            y = input("Yjoueur2 = ")
        marchePas = not(plateau.joue(joueur, x, y))
    pasDeGagnant = not(plateau.checkVictoire(joueur))
    if(pasDeGagnant):
        joueur = 3 - joueur
    plateau.affiche(True)
    
print("joueur n°" + str(joueur) + " gagne")
