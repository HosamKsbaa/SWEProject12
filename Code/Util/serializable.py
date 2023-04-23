import json
from sqlalchemy import inspect
from Util.models2 import Messages
 
class MessagesEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Messages):
            return {
                'MessageId': obj.MessageId,
                'DateTime': obj.DateTime.strftime('%Y-%m-%d %H:%M:%S'),
                'text': obj.text,
            }
        return super().default(obj)
