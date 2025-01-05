from django.urls import path
from myapp.consumers import OrderProgress

ws_urlrouter=[
    path("ws/pizza/<order_id>/", OrderProgress.as_asgi()),
]