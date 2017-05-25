# -*- coding: utf-8 -*-
import numpy as np
from math import exp

class Neurone:
    
    parents = np.array([])
    poids = np.array([])
    biais = 0
 
    def __init__(self, listeParents, listePoids, biais):
        self.parents = listeParents
        self.poids = listePoids
        self.biais = biais   

    def evalue(self, data):
        evals = np.vectorize(lambda x: x.evalue(data))
        entree = evals(self.parents)
        sortie = np.dot(self.poids, entree)
        s = np.vectorize(lambda x: 1 / (1 + exp(- x - self.biais)))
        sortie = s(sortie)
        return sortie

class NeuroneAlpha:
    
    poids = np.array([])
    biais = 0
 
    def __init__(self, listePoids, biais):
        self.poids = listePoids
        self.biais = biais

    def evalue(self, data):
        sortie = np.dot(self.poids, data)
        s = np.vectorize(lambda x: 1 / (1 + exp(- x - self.biais)))
        sortie = s(sortie)
        return sortie

a0 = NeuroneAlpha(np.array([0]*(4*4)).reshape(4,4), 0)