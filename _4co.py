from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
from kafka import KafkaConsumer
from googletrans import Translator
from producer import send_message
from consumer import receive_messages
import crud 



# Set up Kafka consumer
consumer = KafkaConsumer(
    'translated',
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
                text = text.decode('utf-8')
                analyzer = SentimentIntensityAnalyzer()

                # Analyze text
                scores = analyzer.polarity_scores(text)
                crud.create_Analize();
                print(scores)
