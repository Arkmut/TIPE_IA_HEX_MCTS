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
    tailleData = 0
    def __init__(self, forme,tailleData):
        poids0 = np.random.randn(forme[0],tailleData)
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
        resultats = sigmoide(np.dot(self.matPoids[0],data))
        for k in range(1,self.nbCouches):
            resultats = sigmoide(np.dot(self.matPoids[k], resultats))
        return resultats
    
    def liste_sorties(self, data):
        matResult = np.dot(self.matPoids[0], data)
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
        nabla_w = [np.zeros((len(kouche), len(kouche[0]))) for kouche in self.matPoids]
        nabla_b = [np.zeros(len(kouche)) for kouche in self.matBiais]
        for data in miniBatch:
            delta_nabla_b, delta_nabla_w = self.backprop(data)
            print(delta_nabla_w)
            for k in range(self.nbCouches):
                nabla_w[k] = nabla_w[k] + delta_nabla_w[k]
                nabla_b[k] = nabla_b[k] + delta_nabla_b[k]
        n = len(miniBatch)
        for k in range(self.nbCouches):
            self.matPoids[k] = self.matPoids[k] - eta*nabla_w[k]/n
            self.matBiais[k] = self.matBiais[k] - eta*nabla_b[k]/n
    
    
    def backprop(self, data):
        (x, y) = data
        nabla_w = [np.zeros((len(kouche), len(kouche[0]))) for kouche in self.matPoids]
        nabla_b = [np.zeros(len(kouche)) for kouche in self.matBiais]
        resultats, resultsig = self.liste_sorties(x)
        delta = self.deriveeCout(resultsig[-1], y) * sigmoide_prime(resultats[-1])
        nabla_w[-1] = np.dot(delta.reshape(len(delta), 1), resultsig[-2].reshape(1, len(resultsig[-2])))
        nabla_b[-1] = delta
        for l in range(2, self.nbCouches):
            delta = np.dot(self.matPoids[-l+1].transpose(), delta) * sigmoide_prime(resultats[-l])
            nabla_w[-l] = np.dot(delta.reshape(len(delta), 1), resultsig[-l-1].reshape(1, len(resultsig[-l-1])))
            nabla_b[-l] = delta
        return nabla_b, nabla_w
 
    
    def deriveeCout(self, resultats, y):
        return (resultats - y) 
