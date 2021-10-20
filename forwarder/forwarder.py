import paho.mqtt.client as mqtt
import sys

REMOTE_MQTT_HOST = "3.101.64.93"
REMOTE_MQTT_PORT = 32157
REMOTE_MQTT_TOPIC = "faces"

LOCAL_MQTT_HOST = "mosquitto-service"
LOCAL_MQTT_PORT = 1883
LOCAL_MQTT_TOPIC = "faces"

def on_connect_local(client, userdata, flags, rc):
	print("connected to local broker with rc: " + str(rc))
	client.subscribe(LOCAL_MQTT_TOPIC)
	print("subscribed to local topic")

def on_connect_remote(client, userdata, flags, rc):
	print("connected to remote with rc: " + str(rc))

def on_message(client, userdata, msg):
	try:
		print("message received: ")#,str(msg.payload.decode("utf-8")))
		msg = msg.payload
		remote_mgqttclient.publish(REMOTE_MQTT_TOPIC, payload=msg, qos=0, retain=False)
	except:
		print("Unexpected error:", sys.exc_info()[0])

def on_publish(client, userdata, msgid):
	print("message ", msgid, " published to remote server ", REMOTE_MQTT_HOST)

def on_disconnect_local(client, userdata, rc):
	client.loop_stop()

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)

# local_mqttclient.on_disconnect = on_disconnect_local

remote_mqttclient = mqtt.Client()
remote_mqttclient.on_connect = on_connect_remote
#remote_mqttclient.on_publish = on_publish
remote_mqttclient.connect(REMOTE_MQTT_HOST, REMOTE_MQTT_PORT, 60)

local_mqttclient.on_message = on_message

local_mqttclient.loop_forever()
#remote_mqttclient.loop_forever()
