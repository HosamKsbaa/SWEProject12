from kafka import KafkaProducer
from typing import Union
import os

# Create a Kafka producer instance
producer = KafkaProducer(bootstrap_servers=os.environ.get('KAFKA_HOST'), value_serializer=lambda v: str(v).encode('utf-8'))

def send_message(message: Union[str, None], Topic: str = "my-topic"):
    # Send the message to the Kafka topic
    producer.send(Topic, value=message)
