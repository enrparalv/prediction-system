
# --------------------------------------------------------------------------
# Autor del trabajo:
#
# APELLIDOS: PARDO ÁLVAREZ
# NOMBRE: ENRIQUE
# --------------------------------------------------------------------------

import math

def EMAProduction(observation, bu, bc, size):	
    error = 0
    sumDif = 0
    
    for prod,wind in observation:
        
        p = bc+bu*wind
        
        if p < 0:
            p = 0
        
        elif p > 1008:
            p = 1008
            
        AbsDif = abs(prod-p)
        sumDif = sumDif+AbsDif 

    sumObservation = sum(observation[:,0])    
    error = (sumDif/sumObservation) * 100

    return error

def ECMProduction(observation, bu, bc, size):
    error = 0
    sumDif = 0
    
    for prod,wind in observation:
    
        p = bc+bu*wind
        
        if p < 0:
            p = 0
            
        elif p > 1008:
            p = 1008
            
        squareDif = (prod-p)**2
        sumDif = sumDif+squareDif

    sumObservation = sum(observation[:,0])
    sqrtSumSize = math.sqrt(sumDif/size)
    error = ((size*sqrtSumSize)/sumObservation) * 100
    
    return error 
