import json

from channels.generic.websocket import AsyncWebsocketConsumer

class ClassChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel,
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        msg = text_data_json["message"]

        await self.send(text_data=json.dumps({"message": message}))