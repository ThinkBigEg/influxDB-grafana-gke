from influxdb import InfluxDBClient
import random
import datetime
import time

INFLUXDB_HOST = '<EXTERNAL IP>'
INFLUXDB_NAME = 'solar_db'

fixed_interval = 3

while 1:

    timestamp = datetime.datetime.utcnow().isoformat()
    stations = ['S1', 'S2', 'S3']
    energy = random.randint(0,500)

    station_name = stations[random.randint(0,2)]

    client = InfluxDBClient(INFLUXDB_HOST, '8086', '', '', INFLUXDB_NAME)

    json_data = [
        {
            "measurement": "energy_consumed",
            "time": timestamp,
            "tags": {
                "Station": station_name
            },

            "fields": {
                "value": energy
            }
        }
    ]
    bResult = client.write_points(json_data)
    print("Result of Write Data : ", bResult)
    time.sleep(fixed_interval)


