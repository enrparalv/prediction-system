
# --------------------------------------------------------------------------
# Autor del trabajo:
#
# APELLIDOS: PARDO ÁLVAREZ
# NOMBRE: ENRIQUE
# --------------------------------------------------------------------------

import math
import numpy as np
import matplotlib.pyplot as plt

from functions import readData as rd
from functions import errorFunctions as ef


class PredictionSystem():
    
    def __init__(self, observations, predictions, size):
        self.observations = np.array(observations[1:])
        self.predictions = np.array(predictions[1:])
        self.size = size
#        self.avgObsWind = 0
#        self.avgObsProd = 0
#        self.sxx = 0
#        self.sxy = 0
#        self.syy = 0
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
        estimatedValue = bc + bu*wind

        if estimatedValue < 0:
            estimatedValue = 0
        
        elif estimatedValue > 1008:
            estimatedValue = 1008
            
        print("pendiente : ", bu,
              " ordenada en el origen : ",bc)
        print("Mes: ", month)
        
        mFilter = self.observations[np.where(self.observations[:,2]==month)][:,:2]
                
        obs = mFilter[:,:2].astype(int)
#        print("obs : ",obs)
#        obs = [mFilter[:,1].astype(int),mFilter[:,0].astype(int)]
#        print("obs: ",obs)
        EMA = ef.EMAProduction(obs,bu,bc,len(mFilter))
        ECM = ef.ECMProduction(obs,bu,bc,len(mFilter))
        print("EMA : ",EMA)
        print("ECM : ",ECM)
        return estimatedValue
    
    
    
#class PredictionSystemByMonth():
#    
#    def __init__(self, observations, predictions, size):
#        self.observations = np.array(observations[1:])
#        self.predictions = np.array(predictions[1:])
#        self.size = size
#        self.avgObsWind = 0
#        self.avgObsProd = 0
#        self.sxx = 0
#        self.sxy = 0
#        self.syy = 0
#        self.BU = 0
#        self.BC = 0
#    
#    
#    def readData(filename):
#    
#        return rd.readData(filename)    
#    
#    def averageObservationWind(self, month):
#        mFilterW = self.observations[np.where(self.observations[:,2]==month),1]
#        n = len(mFilterW[0])
#        averageWind = 1/n * sum(mFilterW.astype(int)[0])
#        
#        return averageWind
#    
#    def averageObservationProduction(self, month):
#        mFilterP = self.observations[np.where(self.observations[:,2]==month),0]
#        n = len(mFilterP[0])
#        averageProd = 1/n * sum(mFilterP.astype(int)[0])
#        
#        return averageProd
#    
#    def Sxx(self, month):    
#        acum = 0
#        avgWind = self.averageObservationWind(month)
#        mFilterW = self.observations[np.where(self.observations[:,2]==month),1]
#        n = len(mFilterW[0])
#        
#        for wind in mFilterW[0].astype(int):
#            acum = acum + (wind-avgWind)**2
#        
#        sxx = 1/(n-1) * acum 
#        
#        return sxx
#    
#    def Sxy(self, month):
#        acum = 0
#        avgWind = self.averageObservationWind(month)
#        avgProd = self.averageObservationProduction(month)
#
#        mFilter = self.observations[np.where(self.observations[:,2]==month)]
#        n = len(mFilter)     
#        
#        for wind,prod in zip(mFilter[1].astype(int),mFilter[0].astype(int)):
#            acum = acum + (wind-avgWind)*(prod-avgProd)
#        
#        sxy = 1/(n-1) * acum 
#        
#        return sxy
#    
#    def Syy(self, month):
#        acum = 0
#        avgProd = self.averageObservationProduction(month)
#        mFilterP = self.observations[np.where(self.observations[:,2]==month),0]
#        n = len(mFilterP[0])
#        
#        for prod in mFilterP[0].astype(int):
#            acum = acum + (prod-avgProd)**2
#        
#        syy = 1/(n-1) * acum 
#        
#        return syy
#    
#    def betaUno(self, month):
#        sxx = self.Sxx(month)
#        sxy = self.Sxy(month)
#        syy= self.Syy(month)        
#        betaU = (syy-sxx + math.sqrt((syy-sxx)**2 + 4*(sxy)**2)) / (2*sxy)
#        
#        return betaU
#    
#    def betaCero(self, month):
#        betC = self.averageObservationProduction(month) - self.betaUno(month)*self.averageObservationWind(month)
#        
#        return betC
#            
#    def estimatedProductionByMonth(self, wind, month):
#        print("pendiente : ", self.betaUno(month))
#        print("ordenada en el origen : ",self.betaCero(month))
#        print("Mes:   ", month)
#        estimatedValue = self.betaCero(month) + self.betaUno(month)*wind
#        
#        return estimatedValue
        
    
    
    
#    ---------test-----------
        
    
#    a=["2009-11-12","2009-11-15", "2009-08-12", "2009-06-12", "2009-11-16", "2009-01-28", "2009-05-13"]
#    a.sort()
    
#    from operator import itemgetter
#    b = [["2009-11-12", "00:00", "62"],
#    ["2009-11-15", "03:00", "65"],
#    ["2009-11-12", "06:00", "74"],
#    ["2009-11-12", "09:00", "39"],
#    ["2009-11-16", "12:00", "26"],
#    ["2009-11-28", "18:00", "20"]]
#    b.sort(key=itemgetter(2))
#    ' '.join(b[0])
        
#    obs,pred,size = PredictionSystem.readData("test/Meteologica_vacante_ProgC_ProblemaDatos_20190903.txt")
#    predSys = PredictionSystem(obs,pred,size)
#    array=np.asarray(pred)
#    for w,m in zip(array[:,0].astype(int),array[:,1]):
#        print(w)
#        print("Antes del cálculo ......")
#        p = predSys.estimatedProduction(w,m)
#        print("valor estimado :",p)
        
    
#    -------graficos-------
#    x = np.linspace(-1,100,10)
#    y = predSys.betaUno()*x + predSys.betaCero()
#    plt.plot(x, y, '-r')
#    plt.scatter(predSys.observations[:,1].astype(int),predSys.observations[:,0].astype(int))
        
#    condicion de sacar mes de observaciones
#    predSys.observations[np.where(predSys.observations[:,2]=='12'),0]
        
    
    
    
#    obs,pred,size = PredictionSystem.readData("test/Datos_para_Predicciones_por_Mes.txt")
#    predSys = PredictionSystem(obs,pred,size)
#    
#    array=np.asarray(pred)
#    for w,m in array:
#        m=m.split(" ")[0].split("-")[1]
#        p = predSys.estimatedProduction(w.astype(int),m)
#        print("valor estimado :",p)
#    
#        x = np.linspace(-1,100,10)
#        y = predSys.betaUno()*x + predSys.betaCero()
#        plt.plot(x, y, '-r')
#        plt.scatter(predSys.observations[:,1].astype(int),predSys.observations[:,0].astype(int),s=0.2)