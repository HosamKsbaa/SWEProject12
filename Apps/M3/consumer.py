import time
from kafka import KafkaConsumer

# Create a Kafka consumer instance
consumer = KafkaConsumer('my-topic1', bootstrap_servers='localhost:9092', auto_offset_reset='earliest', value_deserializer=lambda m: m.decode('utf-8'))

def receive_messages():
    # Get messages from the Kafka topic
    messages = []

    # Receive messages from the Kafka broker until there are no more messages available.
    while True:
        new_messages = consumer.poll(timeout_ms=1000)
        if not new_messages:
            break
        for _, messages in new_messages.items():
            for message in messages:
                messages.append(message.value)

    return messages



