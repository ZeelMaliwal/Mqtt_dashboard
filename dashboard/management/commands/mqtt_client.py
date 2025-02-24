import json
import ssl
import paho.mqtt.client as mqtt
from django.core.management.base import BaseCommand
from dashboard.models import SensorData
from datetime import datetime as dt

APPEUI = "APPEUI"
APPID  = "APPID"
PSW    = "Password"

class Command(BaseCommand):
    help = 'Start MQTT client to receive data and save it to the Django database'

    def handle(self, *args, **options):
        def on_connect(mqttc, userdata, flags, rc):
            if rc == 0:
                self.stdout.write("Connected to MQTT broker")
                mqttc.subscribe("v3/lairdtemphum@ttn/devices/+/up")
            else:
                self.stdout.write(f"Failed to connect, return code {rc}")

        def on_message(mqttc, userdata, msg):
            try:
                payload = json.loads(msg.payload.decode('utf-8'))
                uplink_message = payload.get('uplink_message')
                if uplink_message:
                    decoded_payload = uplink_message.get('decoded_payload')
                    if decoded_payload:
                        temperature = decoded_payload.get('Temperature')
                        humidity = decoded_payload.get('Humidity')

                        self.stdout.write(f"Temperature: {temperature} °C, Humidity: {humidity} %")

                        # Save to Django model
                        SensorData.objects.create(
                            temperature=temperature,
                            humidity=humidity
                        )
            except (json.JSONDecodeError, KeyError) as e:
                self.stdout.write(f"Error parsing message: {e}")

        mqttc = mqtt.Client()
        mqttc.on_connect = on_connect
        mqttc.on_message = on_message

        mqttc.username_pw_set(APPID, PSW)
        mqttc.tls_set_context(ssl.create_default_context())
        mqttc.connect("eu1.cloud.thethings.network", 8883, 60)

        mqttc.loop_forever()