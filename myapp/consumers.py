from channels.generic.websocket import WebsocketConsumer
import json
from myapp.models import Pizza,Order
from asgiref.sync import async_to_sync
from myapp.utils import give_order_details

class OrderProgress(WebsocketConsumer):
    def connect(self):
        self.room_name=self.scope['url_route']['kwargs']['order_id']
        self.room_group_name = f'order_progress_{self.room_name}'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )   
        order=give_order_details(self.room_name)
       
        self.accept()
        self.send(text_data=json.dumps({"payload": order}))
      
    def order_status(self,event):
        data=event["value"]
        self.send(text_data=json.dumps({"payload": data}))

    def receive(self, text_data=None, bytes_data=None):
        pass

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, 
            self.channel_name
        )