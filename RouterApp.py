import datetime
import sys
import os
from fastapi import FastAPI
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.orm import Session
import sqlalchemy
import crud , database ,schemas
from database  import engine ,SessionLocal
from sqlalchemy import create_engine
import models2

from producer import send_message
from consumer import receive_messages

# Create a FastAPI app instance
models2.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()
		
# Define a route to send a message to the Kafka topic
@app.post('/send-send_message_route2/')
def send_message_route2( message: schemas.MessageCreate ,db: Session = Depends(get_db)):
	return crud.create_Message(db=db, Message=message)



@app.get('/getLastMessage')
async def testGetLastMessage2(db: Session = Depends(get_db)):
	# Send the message to the Kafka topic
	return crud.getLastMessage(db)


@app.get('/getAllMessages')
async def getAllMessages(db: Session = Depends(get_db)):
	# Send the message to the Kafka topic
	return crud.getAllMessages(db)


# Define a route to send a message to the Kafka topic
@app.post('/send-message/{message}')
async def send_message_route(message: str):
    # Send the message to the Kafka topic
    send_message(message)

    return {'message': f'Message sent to Kafka topic: {message}'}

# Define a route to receive messages from the Kafka topic
@app.get('/receive-messages')
async def receive_messages_route():
    messages = receive_messages()
    return {'messages': str(messages)}
