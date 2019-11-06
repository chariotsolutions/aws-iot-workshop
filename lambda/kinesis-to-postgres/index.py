import os
import json
import base64
import psycopg2
from datetime import datetime

host = os.environ["POSTGRESQL_HOSTNAME"] 
user = os.environ["POSTGRESQL_USER"]
password = os.environ["POSTGRESQL_PASSWORD"]
db =  os.environ["POSTGRESQL_DATABASE"]
conn = psycopg2.connect(host=host, database=db, user=user, password=password)

sql = """
    INSERT INTO sensor_data (
        device, temperature, humidity, pressure,
        lux, uva, uvb, uvindex, recorded_at
    ) 
    values (%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

def save_to_postgres(data):

    timestamp = datetime.fromtimestamp(int(data['timestamp']) / 1000.0)

    params = [
        data['device'],
        data['temperature'],
        data['humidity'],
        data['pressure'],
        data['lux'],
        data['uva'],
        data['uvb'],
        data['uvindex'],
        timestamp
    ]
    
    print(sql, params)

    c = conn.cursor()
    c.execute(sql, params)
    conn.commit()
    c.close()

def lambda_handler(event, context):
  # log the event
  print(json.dumps(event))
  
  # decode and log each record
  for record in event['Records']:
      payload = record['kinesis']['data']
      decoded = base64.b64decode(payload)
      data = json.loads(decoded)
      print(data)
      
      save_to_postgres(data)
