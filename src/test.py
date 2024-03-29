
# --------------------------------------------------------------------------
# Autor del trabajo:
#
# APELLIDOS: PARDO ALVAREZ
# NOMBRE: ENRIQUE
# --------------------------------------------------------------------------

import numpy as np

import errorFunctions as ef
import predictionSystem as ps
    
#    ------ test Prediction System ------

obs,pred,size = ps.PredictionSystem.readData("../data/Meteologica_vacante_ProgC_ProblemaDatos_20190903.txt")
predSys = ps.PredictionSystem(obs,pred,size)
month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
array=np.asarray(pred)

print(predSys.betaUno(), " ", predSys.betaCero())

for e in month:
    
    mFilter = predSys.observations[np.where(predSys.observations[:,2]==e)][:,:2]
    obsF = mFilter[:,:2].astype(int)
    ema = ef.EMAProduction(obsF, predSys.BU, predSys.BC, len(mFilter))
    ecm = ef.ECMProduction(obsF, predSys.BU, predSys.BC, len(mFilter))
    print("Mes", int(e), " ", ema, " ", ecm)

for w,m in array:
    
    ms=m.split(" ")[0].split("-")[1]
    p = predSys.estimatedProduction(w.astype(int),ms)
    
    print(m, " ", p[0])
    