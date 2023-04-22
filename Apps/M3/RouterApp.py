import datetime
import sys
import os
from fastapi import FastAPI

from sqlalchemy.orm import Session
from datetime import date 

import models, schemas,producer,consumer

# Create a FastAPI app instance
app = FastAPI()

# Define a route to send a message to the Kafka topic
@app.post('/2send-message/{message}')
async def send_message_route2(db: Session, message: str):
    db_message = models.Messages(message=message,DateTime=date.today())
    db.add( db_message)
    db.commit()
    db.refresh( db_message)
    # send_message(message)

    return  db_message


@app.get('/testGetLastMessage')
async def testGetLastMessage2(db: Session, message: str):
    # Send the message to the Kafka topic
    return db.query(models.Messages).first()


































































































