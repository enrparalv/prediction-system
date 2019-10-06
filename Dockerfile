FROM python:3

ADD src/ /
ADD data/ /

RUN pip3 install numpy

CMD [ "python", "./src/test.py" ]
