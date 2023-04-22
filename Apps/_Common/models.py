
import databases
import ormar
import sqlalchemy
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from .database import Base






    
class Analytics(Base): 
    __tablename__ = "Analytics"
    AnalyticsId =Column(Integer, primary_key=True, index=True)
    neg  = Column(Float)
    neu = Column(Float)
    pos = Column(Float)
    compound= Column(Float)

#https://fastapi.tiangolo.com/tutorial/sql-databases/#create-the-relationships
  
  
class Messages(Base):
  __tablename__ = "Messages"
  MessageId = Column(Integer, primary_key=True, index=True)
  DateTime = Column(DateTime)
  text = Column(String)
  analytics = Column(Integer, ForeignKey("Analytics.AnalyticsId"))
    # https://drive.google.com/file/d/1rvhnZvNokl_rpahXTM_IN2WNq3Qa6boN/view?usp=sharing
    