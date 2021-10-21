FROM ubuntu:latest
# this is needed to make sure we can see the log output
ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONUNBUFFERED=1
WORKDIR /app
RUN export OPENBLAS_CORETYPE=ARMV8
RUN apt-get update
RUN apt-get install -y python3 python3-pip mosquitto-clients
#python3-opencv
#RUN a command to intall the MQTT python client
RUN pip3 install paho-mqtt
RUN pip3 install numpy
# RUN pip3 install opencv-python
RUN pip3 install boto3
# RUN pip3 install Cython
# COPY credentials.py credentials.py 
COPY imageprocessor.py imageprocessor.py 

# CMD python3 /app/imageprocessor.py
CMD ["python3","imageprocessor.py"]