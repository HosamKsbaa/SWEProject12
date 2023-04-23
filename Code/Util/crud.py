from sqlalchemy.orm import Session
from datetime import date 
import json

from Util import  models2, schemas ,producer
from Util.producer import send_message
from Util.serializable import MessagesEncoder


def getAllMessages(db: Session):
    messages = db.query(models2.Messages).all()
    return messages

def getLastMessage(db: Session):
    last_message = db.query(models2.Messages).order_by(models2.Messages.MessageId.desc()).first()
    return last_message

def create_Message(db: Session, Message: schemas.MessageCreate):
    db_message = models2.Messages(text=Message.message,DateTime=date.today(),)
    db.add( db_message)
    db.commit()
    db.refresh( db_message)
    send_message(json.dumps(db_message, cls=MessagesEncoder))

    return  db_message

def create_Analize(db: Session, Analytics:  models2.Analytics):
    db_Analytics = Analytics
    db.add( db_Analytics)
    db.commit()
    db.refresh( db_Analytics)
    # send_message(message)
    return  db_Analytics



def create_Analyze2(db: Session, Analytics: schemas.AnalyticCreate):
    db_Analytics = models2.Analytics(neg=Analytics.neg , neu= Analytics.neu,pos=Analytics.pos, compound=Analytics.compound)
    db.add( db_Analytics)
    db.commit()
    db.refresh( db_Analytics)
    # send_message(message)
    return  db_Analytics
# def create_Message2(db: Session, Message: schemas.MessageCreate):
#     db_message = models2.Messages(text=Message.message,DateTime=date.today(),)
#     db.add( db_message)
#     db.commit()
#     db.refresh( db_message)
#     # send_message(message)

#     return  db_message
