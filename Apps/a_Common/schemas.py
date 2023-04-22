from pydantic import BaseModel

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
        UserId  : int 
        DateTime  : int
        message  : int 
        analytics  : AnalyticsBase 


class MessageCreate(MessageBase):
        pass
class Message(MessageBase):
    id: int
    analytics :int
    class Config:
            orm_mode = True
