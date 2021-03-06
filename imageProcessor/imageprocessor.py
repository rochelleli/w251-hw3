import paho.mqtt.client as mqtt
import numpy as np
import cv2
import sys
import boto3
from credentials import aws_access_key_id,aws_secret_access_key
from botocore.exceptions import ClientError
from botocore.config import Config

LOCAL_MQTT_HOST="mosquitto-service"
LOCAL_MQTT_PORT = 1883
LOCAL_MQTT_TOPIC = "faces"
# LOCAL_MQTT_HOST="localhost"
# LOCAL_MQTT_PORT=32157

#output_dir = "/home/image_processor/images"
count = 0
my_config = Config(region_name = 'us-west-1')
S3_client = boto3.client('s3')
#     's3',
#     aws_access_key_id=aws_access_key_id,
#     aws_secret_access_key=aws_secret_access_key,
# )
def save_img(img_bytes):
    global count
    response = S3_client.put_object(
        Bucket = 'w251-hw3-bucket'
        Body=img_bytes,
        Key='face{:d}.png'.format(count),
        ACL='public-read',
        ContentType='image/png'
    )
    count+=1

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
        # msg = msg.payload
        # decode = np.frombuffer(msg,dtype='uint8')
        # img = cv2.imdecode(decode, flags=1)
        # # msg = np.frombuffer(msg.payload, dtype='uint8')
		# # img = cv2.imdecode(msg, flags=1)

        # cv2.imwrite(f'face_{COUNTER}.png', img)
        # try:
        #     response = S3_client.upload_file(f'face_{COUNTER}.png', 'w251-hw3-bucket', f'face_{COUNTER}.png')
        # except ClientError as e:
        #     print(e)
        # COUNTER+=1

        save_img(msg.payload)
		

		# imgName = output_dir + "face-" + str(counter) + ".png"
		
		# imgfile = open(imgName, 'wb')
		# imgfile.write(msg.payload)
		# imgfile.close()

		# print("Face", str(counter), msg.topic + " received and saved to " + imgName)
		# counter = counter + 1
	except:
		print("Unexpected error:", sys.exc_info()[0])

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect
local_mattclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message

local_mqttclient.loopforever()
