FROM ubuntu:latest
# this is needed to make sure we can see the log output
ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONUNBUFFERED=1
WORKDIR /app
RUN export OPENBLAS_CORETYPE=ARMV8
RUN apt-get update && apt-get install -y python3 python3-pip python3-opencv
#RUN a command to intall the MQTT python client
RUN pip3 install paho-mqtt
RUN pip3 install numpy
RUN pip3 install opencv-python
RUN pip3 install boto3
# RUN pip3 install Cython
COPY credentials.py credentials.py 
COPY imageprocessor.py imageprocessor.py 
# COPY s3_test.py s3_test.py 
# COPY Dockerfile Dockerfile 
# Copy your listener.py file into the container
CMD python3 /app/imageprocessor.py
# CMD python3 /app/s3_test.py