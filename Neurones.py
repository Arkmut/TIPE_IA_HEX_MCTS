# -*- coding: utf-8 -*-
import numpy as np
from math import exp
import time
def getData(pred,data):
    data=pred.evalue(data)
    return data
class Neurone:
    
    parents = np.array([])
    poids = np.array([])
    biais = 0
    sigmoideVect=lambda x:x
    evalVect= lambda x:x
    def __init__(self, listeParents, listePoids, biais):
        self.parents = listeParents
        self.poids = listePoids
        self.biais = biais   
        self.sigmoideVect=np.vectorize(lambda x: 1 / (1 + exp(- x - self.biais)))
        self.evalVect=np.vectorize(getData)
    def evalue(self, data):       
        #entree = self.evalVect(self.parents,data)
        entree=[]
        for i in  range (0,len(self.parents)):
            if(i==0):
                entree=self.parents[i].evalue(data)
            else:
                entree=np.vstack((entree,self.parents[i].evalue(data)))
        sortie = np.dot(self.poids,entree )
        sortie = self.sigmoideVect(sortie)
        return sortie

class NeuroneAlpha:
    
    poids = np.array([])
    biais = 0
 
    def __init__(self, listePoids, biais):
        self.poids = listePoids
        self.biais = biais

    def evalue(self, data):
        sortie = np.dot(data, self.poids)
        s = np.vectorize(lambda x: 1 / (1 + exp(- x - self.biais)))
        sortie = s(sortie)
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
