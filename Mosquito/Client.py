import paho.mqtt.client as mqtt

BROKER_ADDRESS = "localhost"
TOPIC = "test/topic"
MESSAGE = "Hello, Morteza!"

def on_publish(client, userdata, mid):
    print("Message published with mid " + str(mid))

client = mqtt.Client()
client.on_publish = on_publish
client.connect(BROKER_ADDRESS)
client.publish(TOPIC, MESSAGE)
client.disconnect()
