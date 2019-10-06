FROM python:3

ADD Python/predictionSystem.py / 
ADD Python/functions/readData.py /
ADD Python/functions/errorFunctions.py /
ADD Python/test/test.py /
ADD Python/test/Meteologica_vacante_ProgC_ProblemaDatos_20190903.txt /

RUN pip3 install numpy

CMD [ "python", "./Python/test/test.py" ]
