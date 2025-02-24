import json
import ssl
import time
import paho.mqtt.client as mqtt

# MQTT broker settings
broker = "eu1.cloud.thethings.network"
port = 8883
topic = "v3/lairdtemphum@ttn/devices/your_device_id/up"
username = "username"
password = "password"

def on_publish(client, userdata, result):
    print("Data published")

client = mqtt.Client()
client.username_pw_set(username, password)
client.tls_set_context(ssl.create_default_context())  # Use TLS for secure connection
client.on_publish = on_publish
client.connect(broker, port)

for i in range(10):  # Simulate 10 messages
    payload = {
        "uplink_message": {
            "decoded_payload": {
                "Temperature": 20 + i,  # Increment temperature
                "Humidity": 50 + i  # Increment humidity
            }
        }
    }
    client.publish(topic, json.dumps(payload))
    time.sleep(5)  # Wait for 5 seconds before sending the next message

client.disconnect()
