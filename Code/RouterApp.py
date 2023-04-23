from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from Util import crud, schemas, models2
from Util.database import engine, SessionLocal

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

@app.post('/StoreAnalytics/')
def StoreAnalytics( Analytics: schemas.AnalyticCreate ,db: Session = Depends(get_db)):
	return crud.create_Analyze2(db=db, Analytics=Analytics)



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


# Endpoint to get all messages and their analytics
@app.get("/messages")
def get_messages(db: Session = Depends(get_db)):
    messages = db.query(models2.Messages).all()
    message_list = []
    for message in messages:
        analytics = db.query(models2.Analytics).filter(models2.Analytics.MessagesID == message.MessageId).first() 
        message_list.append({"message": message.text,"date": message.DateTime, "analytics": {"neg": analytics.neg, "neu": analytics.neu, "pos": analytics.pos, "compound": analytics.compound,"Translated": analytics.TheTranslatedText}})
    return message_list