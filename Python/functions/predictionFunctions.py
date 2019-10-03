
# --------------------------------------------------------------------------
# Autor del trabajo:
#
# APELLIDOS: PARDO ÁLVAREZ
# NOMBRE: ENRIQUE
# --------------------------------------------------------------------------

#class PredictionFunctions():
    
#    def __init__(self,observations,predictions):
#        self.observations=observations
#        self.predictions=predictions

def averageObservationWind(windValues, size):
    average = 1/size * sum(windValues)
    return average

def averageObservationProduction(productionValues, size):
    average = 1/size * sum(productionValues)
    return average

def Sxx(wind, size):    
    return 0
def Sxy():
    return 0
def Syy():
    return 0
def betaCero():
    return 0
def betaUno():
    return 0
def estimatedWind():
    return 0

def estimatedProduction():
    estimatedValue = betaCero() + betaUno()*estimatedWind() 
    return estimatedValue
