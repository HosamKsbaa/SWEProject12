from kafka import KafkaProducer

# Create a Kafka producer instance
producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: str(v).encode('utf-8'))

def send_message(message: str,Topic: str ="my-topic"):
    # Send the message to the Kafka topic
    producer.send(Topic, value=message)
