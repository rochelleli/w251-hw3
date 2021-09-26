FROM apline

RUN apk update && \
	apk add mosquitto-clients && \
	apk add py3-paho-mqtt

COPY forwarder.py forwarder.py #./
CMD ["python3","forwarder.py"]
