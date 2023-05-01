import json

from channels.generic.websocket import AsyncWebsocketConsumer

class ClassChatConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.class_code = None
        self.class_channel = None
        self.user = None

    async def connect(self):
        print(self.scope['url_route'])
        print(self.scope['url_route']['kwargs'])
        print(self.scope['url_route']['kwargs']['class_code'])
        print(self.scope['url_route']['kwargs']['class_channel'])
        self.class_code = self.scope['url_route']['kwargs']['class_code']
        self.class_channel = self.scope['url_route']['kwargs']['class_code']

        await self.accept()

    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.class_code,
            self.class_channel,
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        msg = text_data_json["message"]

        await self.send(text_data=json.dumps({"message": msg}))