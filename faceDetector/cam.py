import numpy as np
import cv2 as cv
import paho.mqtt.client as mqtt

LOCAL_MQTT_HOST = "localhost" #"broker"
LOCAL_MQTT_PORT = 1883
LOCAL_MQTT_TOPIC = "faces"

def on_publish(client, userdata, result):
	print("Face published.")

local_mqttclient = mqtt.Client()
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.onpublish = on_publish

# the index depends on your camera setup and which one is your USB camera.
# you may need to change to 1 depending on your local config
cap = cv.VideoCapture(0)

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

while(True):
	#Capture frame-by-frame
	ret, frame = cap.read()

	# gray here is the gray frame you will be getting from a camera
	gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)


	for (x,y,w,h) in faces:
	
		# your logic goes here; for instance
		# cut out face from the frame.. 
		# rc,png = cv2.imencode('.png', face)
		# msg = png.tobytes()
		# ...

		face = gray[y:y+h, x:x+w]
		rc, png = cv.imencode('.png', face)
		msg = png.tobytes()
		cv.imshow('face',png)
		
		local_mqttclient.publish(LOCAL_MQTT_TOPIC, msg)

# When everything is done, release the capture
cap.release()
cv.destroyAllWindows()
