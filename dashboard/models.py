from django.db import models
from django.utils import timezone

class SensorData(models.Model):
    temperature = models.FloatField(default=0.0)
    humidity = models.FloatField(default=0.0)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.timestamp}: Temperature: {self.temperature} °C, Humidity: {self.humidity} %"

