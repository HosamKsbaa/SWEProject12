import datetime
import sys
import os
from fastapi import FastAPI
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from ..Utils import crud ,database , models2 ,schemas

from sqlalchemy.orm import Session
from datetime import date 
from Utils.database import SessionLocal, engine

import sqlalchemy
models2.Base.metadata.create_all(bind=engine)

# Create a FastAPI app instance
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# Define a route to send a message to the Kafka topic
@app.post('/send-send_message_route2/',response_model=schemas.Message)
def send_message_route2( message: schemas.MessageCreate ,db: Session = Depends(get_db)):
    return crud.create_Message(db=db, Message=message)



@app.get('/testGetLastMessage',response_model=schemas.Message)
async def testGetLastMessage2(db: Session = Depends(get_db)):
    # Send the message to the Kafka topic
    return crud.get_all_Messages(db)


@app.get('/testGetMessage',response_model=schemas.Message)
async def testGetMessages(db: Session = Depends(get_db)):
    # Send the message to the Kafka topic
    return crud.get_all_Messages(db)

import os


os.chdir("..")
current_directory = os.getcwd()
print(current_directory)