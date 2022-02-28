# w251 Homework 3 - Containers, Kubernetes, and IoT/Edge
The objective of this homework is to buld a lightweight containerized application pipeline with componetns running on the edige, your Jetson, and in the the cloud, a VM in AWS.  The application should be writen in a modular/cloud native way so that it could be run on any edge devce or hub and any cloud VM, or even another type of device connected to some type of storage instead of cloud hosted VM.  In addition, the edge application should be deployed using Kubernetes (K3s for example) on your Jetson and the cloud VM components should run using Docker.

You will build an application that is able to capture faces in a video stream coming from the edge, then transmit them to the cloud via MTQQ and saving these faces for "long term storage".  For the face detector component, we ask that you use OpenCV and write an application that scans the video frames coming from the connected USB camera for faces. When one or more faces are detected in the frame, the application should cut them out of the frame and send via a binary message each.  Your edge applicaiton should use MQTT as your messaging fabric.  As you'll be treating your Jetson as hub, you'll need a broker installed on the Jetson, and that your face detector sends its messages to this broker first. You'll then need another component that receives these messages from the local broker, and sends them to the cloud [MQTT broker]. Because edge applications often use messages to communicate with other local components, you'll need another local listener that just outputs to its log (standard out) that it has received a face message.

In the cloud, you need to provision a lightweight virtual machine (1-2 CPUs and 2-4 G of RAM should suffice) and run an MQTT broker in a Docker container. As discussed above, the faces will need to be sent here as binary messages.  You'll need a second component here that receives the messages and saves the images to to the s3 Object storage, ideally via s3fs (see https://github.com/s3fs-fuse/s3fs-fuse).

## Commands
Commands to deploy yamls and docker commands to build and push onto dockerhub are in the differemt .txt files.

### Order to bring up Containers

1. Brokers
> a. Broker on the Jetson
>
> b. Broker in the cloud
2. Listeners
> a. listener on Jetson (forwarder)
>
> b. listener in the cloud (image processor)
3. Publisher: face detector

## MQTT topics and QoS

### MQTT
MQTT is a messaging protocol for Internet of Things (IoT) that is designed as an extremely lightweight publish/subscribe messaging transport [reference: https://mqtt.org/]. Publishers publish with a topic to the broker and the broker sends the message to subscribers that are subscribed to that topic. The topic name I chose was "faces" because we are sending face data.

### QoS [reference: https://assetwolf.com/learn/mqtt-qos-understanding-quality-of-service]
Quality of Service (QoS) in MQTT messaging is an agreement between sender and receiver on the guarantee of delivering a message.

>There are three levels of QoS:
>- 0 - at most once
>- 1 - at least once
>- 2 - exactly once

I chose to use QoS level 0 because this is not a high stake application and we can tolerate the loss of a message.
