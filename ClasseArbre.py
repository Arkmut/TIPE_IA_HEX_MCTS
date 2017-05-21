# -*- coding: utf-8 -*-
'''Structure d'arbre classique, une racine et une liste d'arbres fils.'''
class Arbre:
    def __init__(self,racine):
        self.racine = racine
        self.fils = []
    
    def ajout(self,elements):
        (self.fils).append(elements)
    
    def affiche(self, nEtage = 0):
        if self.fils == []:
            print("   " * nEtage, self.racine)
        else:
            print("   " * nEtage, self.racine)
            for elt in self.fils:
                elt.affiche(nEtage + 1)
    def nbTot(self,compteur):
        compteur+=1
        if(len(self.fils)==0):
            return compteur
        else:
            for elt in self.fils:
                compteur+=elt.nbTot(compteur)
            return compteur