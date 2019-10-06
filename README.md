# prediction-system
Sistema en Python para la predicción de energía a partir del módulo de la velocidad del viento empleando regresión Deming.

## Descripción del Sistema
En primer lugar el sistema debe cargar un fichero de texto con la siguiente estructura

```
observaciones
YYYY-MM-DD HH:mm 100 10
YYYY-MM-DD HH:mm 100 5
YYYY-MM-DD HH:mm 120 20
predicciones
YYYY-MM-DD HH:mm 20
YYYY-MM-DD HH:mm 12
```

Los 2 últimos valores en el caso del bloque de observaciones son la energía producida y el módulo de la velocidad del viento y para el bloque de predicciones el valor es el del módulo de la velocidad del viento únicamente.

Se ha considerado también que cuando el sistema obtenga como resultado del cálculo de energía un valor negativo devolverá 0 y cuando sobrepase el valor máximo de los datos de observaciones, devolverá este máximo.

### Instalación
Se ha incluido un fichero Dockerfile que contiene lo necesario para la ejecución del sistema. La instrucción para crear la imagen sería la siguiente

```
docker build -t "predictionsystem" .
```

## Ejecución del ejemplo
Para la ejecución del ejemplo basta con ejecutar la siguiente línea

```
docker run predictionsystem python test.py
```

Ésta imagen ejecuta el código del fichero test.py, donde se lee los datos de un fichero de texto y se calcula la recta de regresión. 

Los valores que se imprimen por pantalla son en la primera línea la pendiente y la ordenada en el origen de la recta, a continuación el error por mes que se está cometiendo en ese ajuste respecto a los datos de producción proporcionados, con dos decimales de precisión, primero aparecerá el error medio absoluto en porcentaje
de producción y después el error cuadrático medio en porcentaje de producción y por último la predicción que se daría de producción para cada uno de los valores introducidos en la parte predicciones del fichero de entrada, pero ordenados por fecha.

Un ejemplo de lo que se mostraría sería

```
19.53660609686176   -419.8615288716041
Mes 1   75.56   113.51
Mes 2   56.52   77.01
Mes 3   56.75   76.82
Mes 4   75.95   107.67
Mes 5   53.95   70.61
Mes 6   75.55   114.64
Mes 7   57.67   86.3
Mes 8   49.03   65.27
Mes 9   43.64   61.02
Mes 10   58.43   79.15
Mes 11   61.11   100.52
Mes 12   46.33   65.59
2009-11-12 00:00   791
2009-11-12 06:00   1008
2009-11-12 09:00   342
2009-11-13 00:00   0
2009-11-15 03:00   850
2009-11-16 12:00   88
2009-11-28 18:00   0
```

## Autor

* **Enrique Pardo Álvarez**
