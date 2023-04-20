import time
from kafka import KafkaConsumer

# Create a Kafka consumer instance
consumer = KafkaConsumer('my-topic1', bootstrap_servers='localhost:9092', auto_offset_reset='earliest', value_deserializer=lambda m: m.decode('utf-8'))

def receive_messages():
    # Get messages from the Kafka topic
    messages = []

    # Receive messages from the Kafka broker for 10 seconds.
    timeout = 3  # in seconds
    start_time = time.time()
    while (time.time() - start_time) < timeout:
        new_messages = consumer.poll(timeout_ms=1000)
        for _, message in new_messages.items():
            messages.append(message[0].value)

    return messages
