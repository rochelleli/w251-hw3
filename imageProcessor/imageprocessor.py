import paho.mqtt.client as mqtt
import numpy as np
import cv2
import sys
import boto3
from credentials import aws_access_key_id,aws_secret_access_key
from botocore.exceptions import ClientError
from botocore.config import Config

# LOCAL_MQTT_HOST="mosquitto-service"
# LOCAL_MQTT_PORT = 1883
LOCAL_MQTT_TOPIC = "remote_faces"
LOCAL_MQTT_HOST="0.0.0.0"
LOCAL_MQTT_PORT=#32546

#output_dir = "/home/image_processor/images"

my_config = Config(region_name = 'us-west-2')
S3_client = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
)

def on_connect(client, userdata, flags, rc):
	print("connected to local with rc: " + str(rc))
	client.subscribe(LOCAL_MQTT_TOPIC)
	print("subscribed to topic:", LOCAL_MQTT_TOPIC)

# global variable image counter
COUNTER = 0

def on_message(client, userdata, msg):
	global COUNTER
	global S3_client

	try:
		print("message received")#+str(type(msg))) # ,str(msg.payload.decode("utf-8")))
        # publish the message
        # remote_mqttclient.publish(REMOTE_MQTT_TOPIC,msg.payload)
        # if we wanted to re-publish this message, something like this should work
        msg = msg.payload
        decode = np.frombuffer(msg,dtype='uint8')
        img = cv.imdecode(decode, flags=1)#cv.IMREAD_COLOR)
        # msg = np.frombuffer(msg.payload, dtype='uint8')
		# img = cv2.imdecode(msg, flags=1)

        cv.imwrite(f'face_{COUNTER}.png', img)
        try:
            response = S3_client.upload_file(f'face_{COUNTER}.png', 'w251-hw3-bucket', f'face_{COUNTER}.png')
        except ClientError as e:
            print(e)
        COUNTER+=1
		

		# imgName = output_dir + "face-" + str(counter) + ".png"
		
		# imgfile = open(imgName, 'wb')
		# imgfile.write(msg.payload)
		# imgfile.close()

		# print("Face", str(counter), msg.topic + " received and saved to " + imgName)
		# counter = counter + 1
	except:
		print("Unexpected error:", sys.exc_info()[0])

local_mqttclient = mqtt.client()
local_mqttclient.on_connect = on_connect
local_mattclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message

local_mqttclient.loopforever()
