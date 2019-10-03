
# --------------------------------------------------------------------------
# Autor del trabajo:
#
# APELLIDOS: PARDO ÁLVAREZ
# NOMBRE: ENRIQUE
# --------------------------------------------------------------------------

import math
import numpy as np
from functions import readData as rd


class PredictionSystem():
    
    def __init__(self, observations, predictions, size):
        self.observations = np.array(observations[1:])
        self.predictions = np.array(predictions[1:])
        self.size = size
        self.avgObsWind = 0
        self.avgObsProd = 0
        self.sxx = 0
        self.sxy = 0
        self.syy = 0
        self.BU = 0
        self.BC = 0
        

    def readData(filename):
        
        return rd.readData(filename)
        
    def averageObservationWind(self):
        averageWind = 1/self.size * sum(self.observations[:,1])
        
        return averageWind
    
    def averageObservationProduction(self):
        averageProd = 1/self.size * sum(self.observations[:,0])
        
        return averageProd
    
    def Sxx(self):    
        acum = 0
        avgWind = self.averageObservationWind()
        
        for wind in self.observations[:,1]:
            acum = acum + (wind-avgWind)**2
        
        sxx = 1/(self.size-1) * acum 
        
        return sxx
    
    def Sxy(self):
        acum = 0
        avgWind = self.averageObservationWind()
        avgProd = self.averageObservationProduction()
        
        for wind,prod in zip(self.observations[:,1],self.observations[:,0]):
            acum = acum + (wind-avgWind)*(prod-avgProd)
        
        sxy = 1/(self.size-1) * acum 
        
        return sxy
    
    def Syy(self):
        acum = 0
        avgProd = self.averageObservationProduction()
        
        for prod in self.observations[:,0]:
#            print("antes del calculo :  acum :",acum, "   prod", prod, "  avgProd :  ",avgProd)
            acum = acum + (prod-avgProd)**2
#            print("acum final : ",acum)
        
        syy = 1/(self.size-1) * acum 
#        print("valor Syy: ", syy)
        
        return syy
    
    def betaUno(self):
        sxx = self.Sxx()
        sxy = self.Sxy()
        syy= self.Syy()        
        betaU = (syy-sxx + math.sqrt((syy-sxx)**2 + 4*(sxy)**2)) / (2*sxy)
        
        return betaU
    
    def betaCero(self):
        betC = self.averageObservationProduction() - self.betaUno()*self.averageObservationWind()
        
        return betC
    
#    def estimatedWind(self):
#        
#        
#        return 0
    
    def estimatedProduction(self, wind):
        
        print("pendiente : ", self.betaUno())
        print("ordenada en el origen : ",self.betaCero())
        estimatedValue = self.betaCero() + self.betaUno()*wind
        
        return estimatedValue
    
    
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
#    for x in pred:
#    print("Antes del cálculo ......")
#    p = predSys.estimatedProduction(x)
#    print("valor estimado :",p)
        
#    -------graficos-------
#    x = np.linspace(-1,100,10)
#    y = predSys.betaUno()*x + predSys.betaCero()
#    plt.plot(x, y, '-r')
#    plt.scatter(predictionSys.observations[:,1],predictionSys.observations[:,0])