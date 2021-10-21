# w251 Homework 3 - Containers, Kubernetes, and IoT/Edge

## Commands
Commands to deploy yamls and docker commands to build and push onto dockerhub are in the differemt .txt files.

### Order to bring up Containers

1. Brokers
> a. Broker on the Jetson
> b. Broker in the cloud
2. Listeners
> a. listener on Jetson (forwarder)
> b. listener in the cloud (image processor)
3. Publisher: face detector

## MQTT topics and QoS

### MQTT
MQTT is a messaging protocol for Internet of Things (IoT) that is designed as an extremely lightweight publish/subscribe messaging transport [link: https://mqtt.org/]. Publishers publish with a topic to the broker and the broker sends the message to subscribers that are subscribed to that topic. The topic name I chose was "faces" because we are sending face data.

### QoS [reference: https://assetwolf.com/learn/mqtt-qos-understanding-quality-of-service]
Quality of Service (QoS) in MQTT messaging is an agreement between sender and receiver on the guarantee of delivering a message.

>There are three levels of QoS:
>- 0 - at most once
>- 1 - at least once
>- 2 - exactly once

I chose to use QoS level 0 because this is not a high stake application and we can tolerate the loss of a message.