
# --------------------------------------------------------------------------
# Autor del trabajo:
#
# APELLIDOS: PARDO ÁLVAREZ
# NOMBRE: ENRIQUE
# --------------------------------------------------------------------------

def readData(fileName):
	size = 0
    observationData = []
    predictionData = []
    data = 1

    for line in open(fileName):

        if line == "predicciones":
        	data = 0

    	elif line != "observaciones" and data == 1:
            observationValue = [line.split(" ")[2], line.split(" ")[3]] 
            observationData.append(observationValue)
            size+=1

    	else:
    		predictionValue = line.split(" ")[2] 
            predictionData.append(predictionValue)
    
    return observationData, predictionData, size