import pygame
# -*- coding: utf-8 -*-
''' Un plateau de jeu est representé par une matrice, dont les dimensions sont fixées par la "largeur" du plateau. 
Voici les fonctions dont la classe est constituée:
    -Joue actualise le plateau en rentrant le numéro du joueur aux coordonnées demandées
    -Affiche permet de visualiser le plateau plus facilement avec sa forme de losange (L'affichage est à améliorer)
    -Chemin explore les 6 cases adjacentes pour vérifier s'il existe un chemin d'un bord à l'autre du plateau
    -CheckVictoire renvoie le joueur gagnant de la partie'''

class Plateau:
    # une case est vide (=0) joueur 1 (=1) et joueur 2 (=2)
    mat = []
    taille = 0
    coup = (-1,-1)

    def __init__(self, largeur, matrice, coup):
        self.taille = largeur
        self.coup = coup
        if matrice == []:
            self.mat = [ [0]*self.taille for _ in range(self.taille)]
        else:
            self.mat = matrice
    
    def joue(self, joueur, coup):
        i = coup[0]
        j = coup[1]
        if(self.mat[i][j] == 0):
            self.mat[i][j] = joueur
            self.coup = coup
            return True
        else:
            return False
    
    def lire(self, coord):
        return self.mat[coord[0]][coord[1]]

    def affiche(self):
        s = ""
        for i in range(0, self.taille):
            s += str(i) + "  "
        print("  " * self.taille + "x\y", s)
        for i in range(0, self.taille):
            print("  " * (self.taille - i - 1), i, self.mat[i])

    def affiche2(self):
        pygame.init()
        fenetre= pygame.display.set_mode((900,510))
        fond = pygame.image.load("plateau.png")
        fenetre.blit(fond,(0,0))
        leng = self.taille
        for i in range(leng):
            for j in range(leng):
                x = int(295 + 51.1 * i - 25.5 * j)
                y = int(3 + 44.3 * j)
                if self.mat[i][j] == 1:
                    fenetre.blit(pygame.image.load("rouge.png"),(x, y))
                if self.mat[i][j] == 2:
                    fenetre.blit(pygame.image.load("bleu.png"),(x, y))
        pygame.display.flip()

    #Effectue une copie en mémoire du plateau
    def deepcopy(self):
        newMat = [ligne[:] for ligne in self.mat]
        plat = Plateau(self.taille, newMat, self.coup)
        return plat
    
    def chemin(self, joueur, xDepart, yDepart, dejaVu):
        dejaVu.append((xDepart, yDepart))
        #Cas de base, on est arrivé de l'autre coté du plateau
        if((yDepart == self.taille-1 and joueur == 1) or (xDepart == self.taille-1 and joueur == 2)):
            return True
        else:
            #On créé la liste des cases adjacentes non visitées
            ptsAdja = []
            if(xDepart < self.taille-1):
                if not((xDepart+1, yDepart) in dejaVu):
                    ptsAdja.append((xDepart+1, yDepart))
                if (yDepart < self.taille-1) and not((xDepart+1, yDepart+1) in dejaVu):
                    ptsAdja.append((xDepart+1, yDepart+1))
            if(xDepart > 0):
                if not((xDepart-1, yDepart) in dejaVu):
                    ptsAdja.append((xDepart-1, yDepart))
                if(yDepart > 0) and not((xDepart-1, yDepart-1) in dejaVu):
                    ptsAdja.append((xDepart-1, yDepart-1))
            if(yDepart < self.taille-1) and not((xDepart, yDepart+1) in dejaVu):
                ptsAdja.append((xDepart, yDepart+1))
            if(yDepart > 0) and not((xDepart, yDepart-1) in dejaVu):
                ptsAdja.append((xDepart, yDepart-1))
            #On applique récursivement chemin Ă  chaque case de la liste contenant un pion de joueur
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