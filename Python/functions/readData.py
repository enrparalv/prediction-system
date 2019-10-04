
# --------------------------------------------------------------------------
# Autor del trabajo:
#
# APELLIDOS: PARDO ÁLVAREZ
# NOMBRE: ENRIQUE
# --------------------------------------------------------------------------
import sys
sys.path.append('..')

from operator import itemgetter

def readData(fileName):
    size = 0
    observationData = []
    predictionData = []
    data = 0

    for line in open(fileName):
        production=0
        wind=0
        month=0
        
        if line == "predicciones\n":
        	data += 1

        elif line != "observaciones" and data == 0:
            spLine = line.split(" ")
            
            if len(spLine) == 4:
                production = int(spLine[2])
                wind = int(spLine[3].rstrip())
                month = spLine[0].split("-")[1]

            observationValue = [production, wind, month] 
            observationData.append(observationValue)
            size+=1

        else:
            spLine2 = line.split(" ")
            predictionValue = int(spLine2[2].rstrip()) 
            date = ' '.join([spLine2[0],spLine2[1]])
            predValDate = [predictionValue,date]
            predictionData.append(predValDate)

    predictionData.sort(key=itemgetter(1))        
    
    return observationData, predictionData, size
