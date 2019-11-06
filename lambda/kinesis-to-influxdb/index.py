import os
import json
import base64
from influxdb import InfluxDBClient

host = os.environ["INFLUXDB_HOSTNAME"] 
user = os.environ["INFLUXDB_USER"]
password = os.environ["INFLUXDB_PASSWORD"]
db =  os.environ["INFLUXDB_DATABASE"]
client = InfluxDBClient(host, 8086, user, password, db)

# https://docs.influxdata.com/influxdb/v1.7/concepts/crosswalk/
# https://github.com/influxdata/influxdb-python#examples
def save_to_influx(dict):
    """Save a dictionary of measurements to InfluxDB"""
    data_points = []

    measurements = list(dict.keys())
    # device and timestamp are recorded with every measurement
    measurements.remove('device')
    measurements.remove('timestamp')

    # build structure to insert into InfluxDB
    for measurement in measurements:
        data = {}
        data['measurement'] = measurement
        data['tags'] = {
            'device': dict['device']
        }
        # convert string milliseconds to int nano-seconds
        data["time"] = int(float(dict['timestamp']) * 1000) # nano-seconds utc
        data["fields"] = { "value": float(dict[measurement])}

        print(data)
        data_points.append(data)

    # write multiple records at once
    client.write_points(data_points, time_precision='u')
    print(f'Saved {len(data_points)} measurements to InfluxDB')

def lambda_handler(event, context):
  # log the event
  print(json.dumps(event))
  
  # decode and log each record
  for record in event['Records']:
      payload = record['kinesis']['data']
      decoded = base64.b64decode(payload)
      data = json.loads(decoded)
      print(data)
      
      save_to_influx(data)
