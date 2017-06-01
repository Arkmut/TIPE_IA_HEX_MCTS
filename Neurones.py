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
