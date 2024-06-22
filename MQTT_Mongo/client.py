import paho.mqtt.client as mqtt
import time
import json
import random



BROKER_HOST = "localhost"
PORT = 1883
TOPIC = "sensor/status"
# TOPIC = "test/topic"
MESSAGE = "Hello, MQTT!"

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")


def publish_message(client, TOPIC, MESSAGE):
    status = random.randint(0, 6)
    message = json.dumps({'status': status, 'timestamp': time.time()})
    client.publish(TOPIC, message)
    # result = client.publish(TOPIC, MESSAGE)
    # status = result[0]
    # if status == 0:
    #      print(f"Sent `{MESSAGE}` to topic `{TOPIC}`")
    # else:
    #     print(f"Failed to send message to topic {TOPIC}")


def mqtt_connect():
    client = mqtt.Client()
    client.on_connect = on_connect 
    client.connect(BROKER_HOST, PORT, 60)
    client.loop_start()

    try:
        while True:
            # publish_message(client)
            print('Connected to MQTT broker')
            publish_message(client, TOPIC, MESSAGE)
            time.sleep(1)

    except KeyboardInterrupt:
        client.loop_stop()
        print('Disconnected from MQTT broker')

if __name__ == "__main__":
    mqtt_connect()