# import paho.mqtt.client as mqtt
# import json

# BROKER_HOST = "localhost"
# PORT = 1883
# TOPIC = "sensor/status"

# def on_connect(client, userdata, flags, rc):
#     print(f"Connected with result code {rc}")
#     client.subscribe(TOPIC)

# def on_message(client, userdata, msg):
#     try:
#         payload = json.loads(msg.payload.decode())
#         print(f"Received message: {payload}")
#     except json.JSONDecodeError as e:
#         print(f"Failed to decode JSON: {e}")

# def mqtt_subscribe():
#     client = mqtt.Client()
#     client.on_connect = on_connect
#     client.on_message = on_message

#     client.connect(BROKER_HOST, PORT, 60)
#     client.loop_forever()

# if __name__ == "__main__":
#     mqtt_subscribe()


import paho.mqtt.client as mqtt
import json
import time
from pymongo import MongoClient
from flask import Flask, request, jsonify

BROKER_HOST = "localhost"
PORT = 1883
TOPIC = "sensor/status"

# Initialize MongoDB client
mongo_client = MongoClient("mongodb://localhost:27017/")
db = mongo_client.mqtt
collection = db.messages

# Initialize Flask app
app = Flask(__name__)

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        collection.insert_one(payload)
        print(f"Received and stored message: {payload}")
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")

def mqtt_subscribe():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER_HOST, PORT, 60)
    client.loop_start()

# Define endpoint to get count of statuses within a time range
@app.route('/status_count', methods=['GET'])
def status_count():
    start_time = float(request.args.get('start'))
    end_time = float(request.args.get('end'))
    print("##################### ",start_time, end_time)
    pipeline = [
        {"$match": {"timestamp": {"$gte": start_time, "$lte": end_time}}},
        {"$group": {"_id": "$status", "count": {"$sum": 1}}}
    ]
    
    results = list(collection.aggregate(pipeline))
    response = {str(result['_id']): result['count'] for result in results}
    
    return jsonify(response)

if __name__ == "__main__":
    mqtt_subscribe()
    app.run(port=5000)

