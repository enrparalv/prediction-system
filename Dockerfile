FROM python:3

ADD src /src
ADD data /data

RUN pip3 install numpy

CMD [ "python", "./src/test.py" ]
