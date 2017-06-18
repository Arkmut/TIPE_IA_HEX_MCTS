#coding: utf-8 

import numpy as np
import random as rd

def sigmoide(z):
    return 1 / (1 + np.exp(-z))

def sigmoide_prime(z):
    return sigmoide(z) * (1 - sigmoide(z))


#class Neurone:
#    
#    poids = np.empty(0)
#    biais = 0
#    nbEntrees = 0
# 
#    def __init__(self, listePoids, biais):
#        self.poids = listePoids
#        self.biais = biais
#        self.nbEntrees = len(self.poids)
#
#    def evalue(self, data):
#        sortie = np.dot(data, self.poids)
#        return sortie


class Reseau:

    matPoids = []
    matBiais = []
    nbCouches = 0

    def __init__(self, forme):
        poids0 = np.random.randn(forme[0])
        biais0 = np.random.randn(forme[0])
        self.matPoids = [poids0]
        self.matBiais = [biais0]
        for k in range(1, len(forme)):
            poidsK = np.random.randn(forme[k], forme[k-1])
            biaisK = np.random.randn(forme[k])
            self.matPoids.append(poidsK)
            self.matBiais.append(biaisK)
        self.nbCouches = len(forme)
    
    def evalue(self, data):
        resultats = sigmoide(data * self.matPoids[0])
        for k in range(1, self.nbCouches):
            resultats = sigmoide(np.dot(self.matPoids[k], resultats))
        return resultats
    
    def liste_sorties(self, data):
        matResult = np.array(data) * self.matPoids[0]
        matResultSig = sigmoide(matResult)
        matResult = [matResult]
        matResultSig = [matResultSig]
        for k in range(1, self.nbCouches):
            evalTemp = np.dot(self.matPoids[k], matResultSig[-1])
            matResult.append(evalTemp)
            matResultSig.append(sigmoide(evalTemp))
        return matResult, matResultSig
    
    def sgd(self, donnees, taille, eta, nb_tour):
        for i in range(nb_tour):
            rd.shuffle(donnees)
            miniBatch = donnees[:taille]
            self.update(miniBatch, eta)

    def update(self, miniBatch, eta):
        nabla_w = [np.zero(len(kouche), len(kouche[0])) for kouche in self.matPoids]
        nabla_b = [np.zero(len(kouche)) for kouche in self.matBiais]
        for data in miniBatch:
            delta_nabla_w, delta_nabla_b = self.backprop(data)
            for k in len(nabla_w):
                nabla_w[k] = nabla_w[k] + delta_nabla_w[k]
                nabla_b[k] = nabla_b[k] + delta_nabla_b[k]
        n = len(miniBatch)
        for k in len(self.couches):
            self.matPoids[k] = self.matPoids[k] - eta*nabla_w[k]/n
            self.matBiais[k] = self.matBiais[k] - eta*nabla_b[k]/n
    
    
    def backprop(self, data):
        (x, y) = data
        nabla_w = [np.zero(len(kouche), len(kouche[0])) for kouche in self.matPoids]
        nabla_b = [np.zero(len(kouche)) for kouche in self.matBiais]
        resultats, resultsig = self.liste_sorties(x)
        delta = self.deriveeCout(resultsig[-1], y) * sigmoide_prime(resultats[-1])
        nabla_w[-1] = np.dot(delta.reshape(len(delta), 1), resultsig[-2].reshape(1, len(delta)))
        nabla_b[-1] = delta
        for l in range(2, self.nbCouches):
            delta = np.dot(self.matPoids[-l+1].transpose(), delta) * sigmoide_prime(resultats[-l])
            nabla_w[-l] = np.dot(delta.reshape(len(delta), 1), resultsig[-l-1].reshape(1, len(delta)))
            nabla_b[-l] = delta
        return nabla_b, nabla_w
 
    
    def deriveeCout(self, resultats, y):
        return (resultats - y) 