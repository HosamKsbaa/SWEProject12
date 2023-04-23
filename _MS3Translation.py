from kafka import KafkaConsumer
import googletrans
from googletrans import Translator

from Util.producer import send_message
from Util.consumer import receive_messages



translator = Translator()

# Set up Kafka consumer
consumer = KafkaConsumer(
    'my-topic',
    bootstrap_servers=['localhost:9092'],
    # group_id='my-group'
)




# Receive messages from the Kafka broker until there are no more messages available.
while True:
    new_messages = consumer.poll(timeout_ms=1000)
    if new_messages:
        for _, messages in new_messages.items():
            for message in messages:
                text = message.value
                if translator.detect(text).lang != "en":
                    text = text.decode('utf-8')
                    # Translate text to English
                    text = translator.translate(text, dest='en').text
                    
                send_message(text,Topic= "translated")
                with open('englishText2.txt', 'a', encoding='utf-8') as file:
                    # Write translated text to file
                    print(str(text)+ "\n")
                    file.write(str(text)+ "\n")
