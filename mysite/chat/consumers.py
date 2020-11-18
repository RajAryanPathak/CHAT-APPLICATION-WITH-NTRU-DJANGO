import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.name = self.scope['url_route']['kwargs']['name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):

        text_data_json = json.loads(text_data)
        print(type(text_data_json))
        message = text_data_json['message']
        name = text_data_json['name']
        print(name)
        print("encrypt message here")
        print('before sending to layer at chat/consumer receive', message)
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'name': name,
                'message': message
            }

        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        name = event['name']
        print(name)
        print('data sending to other chat at chat/consumer receive', message)
        # Send message to WebSocket
        await self.send(text_data=json.dumps({

            'name': name,
            'message': message
        }))
