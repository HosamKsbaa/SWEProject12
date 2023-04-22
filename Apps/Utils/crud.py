from sqlalchemy.orm import Session
from datetime import date 

import models2, schemas


def get_Message(db: Session):
    return db.query(models2.Messages).first()

def get_all_Messages(db: Session):
    return db.query(models2.Messages).all()

def create_Message(db: Session, Message: schemas.MessageCreate):
    db_message = models2.Messages(text=Message.message,DateTime=date.today(),)
    db.add( db_message)
    db.commit()
    db.refresh( db_message)
    # send_message(message)

    return  db_message

#http://localhost:5050
#   PGADMIN_DEFAULT_EMAIL: raj@nola.com
#       PGADMIN_DEFAULT_PASSWORD: admin