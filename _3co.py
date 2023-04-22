from kafka import KafkaConsumer
import googletrans
from googletrans import Translator

translator = Translator()

# Set up Kafka consumer
consumer = KafkaConsumer(
    'my-topic',
    bootstrap_servers=['localhost:9092'],
    # group_id='my-group'
)


messagesList = []

# Receive messages from the Kafka broker until there are no more messages available.
while True:
    new_messages = consumer.poll(timeout_ms=1000)
    if new_messages:
        for _, messages in new_messages.items():
            for message in messages:
                text = message.value
                if translator.detect(text).lang != "en":
                    # Translate text to English
                    text = translator.translate(text, dest='en').text
                with open('englishText2.txt', 'a', encoding='utf-8') as file:
                    # Write translated text to file
                    file.write(str(text)+ "\n")


# Continuously read messages from Kafka topic and translate them
# while True:
#     # Wait for new messages
#     for message in consumer.poll(timeout_ms=1000):
#         if message is not None:
#             for msg in message:
#                 text = msg
#                 if translator.detect(text).lang != "en":
#                     # Translate text to English
#                     text = translator.translate(text, dest='en').text
#                 with open('englishText2.txt', 'a', encoding='utf-8') as file:
#                     # Write translated text to file
#                     print("A7aaaaaaaaaaaaaaaaaaaaaaaa")
#                     print(text)
#                     file.write(str(text)+ "\n")
