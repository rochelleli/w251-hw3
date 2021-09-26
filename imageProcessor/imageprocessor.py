import paho.mqtt.client as mqtt
import numpy as np
import cv2

LOCAL_MQTT_HOST = "localhost"
LOCAL_MQTT_PORT = 1883
LOCAL_MQTT_TOPIC = "remote_faces"

output_dir = "/home/image_processor/images"

def on_connect(client, userdata, flags, rc):
	print("connected to local with rc: " + str(rc))
	client.subscribe(LOCAL_MQTT_TOPIC)
	print("subscribed to topic:", LOCAL_MQTT_TOPIC)

# global variable image counter
counter = 0

def on_message(client, userdata, msg):
	global counter

	try:
		msg = np.frombuffer(msg.payload, dtype='uint8')
		img = cv2.imdecode(msg, flags=1)

		imgName = output_dir + "face-" + str(counter) + ".png"
		
		imgfile = open(imgName, 'wb')
		imgfile.write(msg.payload)
		imgfile.close()

		print("Face", str(counter), msg.topic + " received and saved to " + imgName)
		counter = counter + 1
	except:
		print("Unexpected error:", sys.exc_info()[0])

local_mqttclient = mqtt.client()
local_mqttclient.on_connect = on_connect
local_mattclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message

local_mqttclient.loopforever()
