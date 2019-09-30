
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
    data = 0

    for line in open(fileName):
        production=0
        wind=0
        
        if line == "predicciones\n":
        	data += 1

        elif line != "observaciones" and data == 0:
            spLine = line.split(" ")
            
            if len(spLine) == 4:
                production = int(spLine[2])
                wind = spLine[3].rstrip()

            observationValue = [production, wind] 
            observationData.append(observationValue)
            size+=1

        else:
            predictionValue = line.split(" ")[2].rstrip() 
            predictionData.append(predictionValue)
            
    return observationData, predictionData, size
