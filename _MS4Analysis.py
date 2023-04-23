from Util.database  import SessionLocal
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
from kafka import KafkaConsumer
from googletrans import Translator
from Util.producer import send_message
from Util.consumer import receive_messages
import Util.crud 
import Util.models2
import datetime
import sys
import os
from fastapi import FastAPI
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.orm import Session
import sqlalchemy
from Util import crud , database ,schemas ,models2
from Util.database  import engine ,SessionLocal
from sqlalchemy import create_engine
import Util.models2

from Util.producer import send_message
from Util.consumer import receive_messages

models2.Base.metadata.create_all(bind=engine)

# Set up Kafka consumer
consumer = KafkaConsumer(
    'translated',
    bootstrap_servers=['localhost:9092'],
    # group_id='my-group'
)

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()

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
                crud.create_Analize(db= Depends(get_db),Analytics= models2.Analytics(neg= scores['neg'],neu = scores['neu'] ,pos = scores['pos'] , compound  = scores['compound'] ) );
                print(scores)