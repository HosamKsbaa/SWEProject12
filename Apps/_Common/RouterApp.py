from fastapi import FastAPI, Depends
from producer import send_message
from consumer import receive_messages
from sqlalchemy.orm import Session
from _Common import models, schemas
import models
from database import engine, SessionLocal
from pydantic import BaseModel, Field

# Create a FastAPI app instance
app = FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

class Message:
    MessageId : int = Field(min_length=1)
    DateTime :  str =  Field(min_length=1)
    text : str 
    analytics : int 

MESSAGES = []

@app.get("/")
def read_api(db:Session = Depends(get_db)):
    return db.query(models.Messages).all()

@app.post("/")
def create_message(message: Message, db:Session = Depends(get_db)):
    message_model = models.Messages()
    message_model.text = message.text
    
































































































