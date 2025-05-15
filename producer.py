import pandas as pd
from kafka import KafkaProducer
from time import sleep
from json import dumps
import json
producer = KafkaProducer(bootstrap_servers='54.158.178.162:9092', #change ip here
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

df = pd.read_csv('C:/Users/amitk/Desktop/Kafka_Project/indexProcessed.csv')
for i in range(0,50):
    dict_stock=df.sample(1).to_dict(orient="records")[0]
    producer.send('demo_test1', value=dict_stock)
    sleep(1)
producer.flush()