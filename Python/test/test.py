
# --------------------------------------------------------------------------
# Autor del trabajo:
#
# APELLIDOS: PARDO ÁLVAREZ
# NOMBRE: ENRIQUE
# --------------------------------------------------------------------------

import sys
sys.path.append('..')

import math
import numpy as np
import matplotlib.pyplot as plt

from functions import readData as rd
from functions import errorFunctions as ef
from predictionSystem import PredictionSystem

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
        
    
    
#    ------ test Prediction System ------
obs,pred,size = PredictionSystem.readData("Datos_para_Predicciones_por_Mes.txt")
predSys = PredictionSystem(obs,pred,size)

array=np.asarray(pred)
for w,m in array:
    m=m.split(" ")[0].split("-")[1]
    p = predSys.estimatedProduction(w.astype(int),m)
    print("valor estimado :",p)

    x = np.linspace(-1,100,10)
    y = predSys.betaUno()*x + predSys.betaCero()
    plt.plot(x, y, '-r')
    plt.scatter(predSys.observations[:,1].astype(int),predSys.observations[:,0].astype(int),s=0.2)