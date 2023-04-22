from fastapi import FastAPI
from producer import send_message
from consumer import receive_messages

# Create a FastAPI app instance
app = FastAPI()

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
