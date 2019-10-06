
# --------------------------------------------------------------------------
# Autor del trabajo:
#
# APELLIDOS: PARDO ALVAREZ
# NOMBRE: ENRIQUE
# --------------------------------------------------------------------------

import math
import numpy as np

import readData as rd
import errorFunctions as ef


class PredictionSystem():
    
    def __init__(self, observations, predictions, size):
        self.observations = np.array(observations[1:])
        self.predictions = np.array(predictions[1:])
        self.size = size      
        self.BU = 0
        self.BC = 0


    def readData(filename):
        
        return rd.readData(filename)

        
    def averageObservationWind(self):
        averageWind = (1/self.size) * sum(self.observations[:,1].astype(int))
        
        return averageWind

    
    def averageObservationProduction(self):
        averageProd = (1/self.size) * sum(self.observations[:,0].astype(int))
        
        return averageProd

    
    def Sxx(self):    
        acum = 0
        avgWind = self.averageObservationWind()
        
        for wind in self.observations[:,1].astype(int):
            acum = acum + (wind-avgWind)**2
        
        sxx = 1/(self.size-1) * acum 
        
        return sxx

    
    def Sxy(self):
        acum = 0
        avgWind = self.averageObservationWind()
        avgProd = self.averageObservationProduction()
        
        for wind,prod in zip(self.observations[:,1].astype(int),self.observations[:,0].astype(int)):
            acum = acum + (wind-avgWind)*(prod-avgProd)
        
        sxy = 1/(self.size-1) * acum 
        
        return sxy

    
    def Syy(self):
        acum = 0
        avgProd = self.averageObservationProduction()
        
        for prod in self.observations[:,0].astype(int):
            acum = acum + (prod-avgProd)**2
        
        syy = 1/(self.size-1) * acum 
        
        return syy

    
    def betaUno(self):
        sxx = self.Sxx()
        sxy = self.Sxy()
        syy= self.Syy()        
        betaU = (syy-sxx + math.sqrt((syy-sxx)**2 + 4*(sxy)**2)) / (2*sxy)
        
        self.BU = betaU
        
        return betaU

    
    def betaCero(self):
        betaC = self.averageObservationProduction() - self.betaUno()*self.averageObservationWind()
        
        self.BC = betaC
        
        return betaC   

    
    def estimatedProduction(self, wind, month):
        bc = self.betaCero()
        bu = self.betaUno()
        estimatedValue = int(bc + bu*wind)

        if estimatedValue < 0:
            estimatedValue = 0
        
        elif estimatedValue > 1008:
            estimatedValue = 1008
                    
        mFilter = self.observations[np.where(self.observations[:,2]==month)][:,:2]
                
        obs = mFilter[:,:2].astype(int)

        EMA = ef.EMAProduction(obs,bu,bc,len(mFilter))
        ECM = ef.ECMProduction(obs,bu,bc,len(mFilter))

        return estimatedValue, EMA, ECM

    