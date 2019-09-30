
# --------------------------------------------------------------------------
# Autor del trabajo:
#
# APELLIDOS: PARDO ÁLVAREZ
# NOMBRE: ENRIQUE
# --------------------------------------------------------------------------

import math

def EMAProduction(observations, predictions, size):
	error = 0
	sumDif = 0

	for O,P in zip(observations,predictions):

		sumAbsDif = abs(O-P)
		sumDif = sumDif+sumAbsDif 
	
	sumObservation = sum(observations)
	error = 100/sumObservation * sumDif 

	return error

def ECMProduction(observations, predictions, size):
	error = 0
	sumDif = 0

	for O,P in zip(observations,predictions):

		squareDif = (O-P)**2
		sumDif = sumDif+squareDif

	sumObservation = sum(observations)
	sqrtSumSize = math.sqrt(sumDif/size)
	error = 100*size/sumObservation * sqrtSumSize

	return error 
	