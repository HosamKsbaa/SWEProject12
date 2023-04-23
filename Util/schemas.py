from pydantic import BaseModel
from typing import Optional

from pydantic import BaseModel, Field
import uuid

class AnalyticsBase(BaseModel): 
    neg   : int 
    neu  : int 
    pos  : int 
    compound : int 

class AnalyticCreate(AnalyticsBase): 
    pass
class Analytics(AnalyticsBase): 
    id: int
    class Config:
            orm_mode = True


#https://fastapi.tiangolo.com/tutorial/sql-databases/#create-the-relationships
  

class MessageBase(BaseModel):
        # UserId  : int 
        # DateTime  : int
        message  : Optional[str] 

class MessageCreate(MessageBase): 
        pass


class Message(MessageBase):
        id: int = Field(default_factory=lambda: uuid.uuid4().int)
        analytics : Optional[int]

        class Config:
                orm_mode = True
