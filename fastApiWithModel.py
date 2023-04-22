from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

app = FastAPI()

SQLALCHEMY_DATABASE_URL = "sqlite:///./messages.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Message(BaseModel):
    MessageId: int = Field(primary_key=True)
    text: str
    analytics: int

class DBMessage(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    MessageId = Column(Integer)
    text = Column(String)
    analytics = Column(Integer)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/send-messages/")
async def create_message(message: Message, db: Session = Depends(get_db)):
    db_message = DBMessage(**message.dict())
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return {"message": f"Message {db_message.id} created"}

@app.get("/messages/")
async def get_messages(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    messages = db.query(DBMessage).offset(skip).limit(limit).all()
    return messages
