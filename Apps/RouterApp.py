import datetime
import sys
import os
from fastapi import FastAPI
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.orm import Session
import sqlalchemy
import crud , database ,models2 ,schemas
from database  import engine ,SessionLocal
from sqlalchemy import create_engine


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
	x=crud.create_Message(db=db, Message=message)
	return 



@app.get('/getLastMessage')
def testGetLastMessage2(db: Session = Depends(get_db)):
	# Send the message to the Kafka topic
	x = crud.getAllMessages(db)
	return x


@app.get('/getAllMessages')
def getAllMessages(db: Session = Depends(get_db)):
	# Send the message to the Kafka topic
	x=crud.get_Message(db)
	return x



