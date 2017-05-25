# -*- coding: utf-8 -*-
import numpy as np
from math import exp
import time

class Neurone:
    
    predecesseur = np.array([])
    poids = np.array([])
    biais = 0
    sigmoide = lambda x: x
 
    def __init__(self, listePredecesseur, listePoids, biais):
        self.predecesseur = listePredecesseur
        self.poids = listePoids
        self.biais = biais
        self.sigmoide = np.vectorize(lambda x: 1 / (1 + exp(- x - self.biais)))

    def evalue(self, data):
        entree = [self.predecesseur[0].evalue(data)]
        for k in range(1, len(self.predecesseur)):
            np.concatenate((entree, [self.predecesseur[k].evalue(data)]))
        sortie = np.dot(self.poids, entree)
        sortie = self.sigmoide(sortie)
        return sortie

class NeuroneAlpha:
    
    poids = np.array([])
    biais = 0
 
    def __init__(self, listePoids, biais):
        self.poids = listePoids
        self.biais = biais
        self.sigmoide = np.vectorize(lambda x: 1 / (1 + exp(- x - self.biais)))


    def evalue(self, data):
        sortie = np.dot(data, self.poids)
        sortie = self.sigmoide(sortie)
        return sortie

tmps1=time.clock()
tailleI=81
tailleJ=81
listeP=[]
nbP=10
for i in range (0,nbP):
    a0 = NeuroneAlpha(np.array([0]*(tailleI*tailleJ)).reshape(tailleI,tailleJ), 0)
    listeP.append(a0)
b=Neurone(listeP,np.array([0]*(nbP*1)).reshape(1,nbP),0)
tmps2=time.clock()
print(b.evalue(np.array([0]*(tailleJ*1))),"temps:",tmps2-tmps1)
