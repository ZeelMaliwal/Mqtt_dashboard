# Generated by Django 5.1 on 2024-08-28 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_sensordata_timestamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sensordata',
            old_name='acceleration_sensor3',
            new_name='acceleration_x',
        ),
        migrations.RenameField(
            model_name='sensordata',
            old_name='humidity_sensor1',
            new_name='acceleration_y',
        ),
        migrations.RenameField(
            model_name='sensordata',
            old_name='humidity_sensor2',
            new_name='acceleration_z',
        ),
        migrations.RenameField(
            model_name='sensordata',
            old_name='humidity_sensor3',
            new_name='humidity',
        ),
        migrations.RenameField(
            model_name='sensordata',
            old_name='temperature_sensor1',
            new_name='temperature',
        ),
        migrations.RemoveField(
            model_name='sensordata',
            name='temperature_sensor2',
        ),
        migrations.RemoveField(
            model_name='sensordata',
            name='temperature_sensor3',
        ),
    ]
