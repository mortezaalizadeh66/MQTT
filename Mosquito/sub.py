import paho.mqtt.client as mqtt

BROKER_ADDRESS = "localhost"
TOPIC = "test/topic"

def on_connect(client, userdata, flags, rc):
    print("Subscriber 1 connected with result code " + str(rc))
    client.subscribe(TOPIC)

def on_message(client, userdata, message):
    print("Message received by Subscriber 1 on topic " + message.topic + ": " + str(message.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER_ADDRESS)
client.loop_forever()
