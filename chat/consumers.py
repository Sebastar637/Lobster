import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Chat, ChatRoom

class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = 'chat_%s' % self.room_id

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']
        avatar = text_data_json['avatar']

        #Buscar el objeto Room
        room = await database_sync_to_async(ChatRoom.objects.get)(id=self.room_id)
        #Creo el objeto chat
        chat = Chat(
            content=message,
            user=self.scope['user'],
            room=room
        )
        #Guardo el mensaje creado en el objeto anterior
        await database_sync_to_async(chat.save)()

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chatroom_message',
                'message': message,
                'username': username,
                'avatar': avatar,
            }
        )

    async def chatroom_message(self, event):
        message = event['message']
        username = event['username']
        avatar = event['avatar']

        text_data = json.dumps({
            'message': message,
            'username': username,
            'avatar': avatar,
        })

        await self.send(text_data)

    pass
