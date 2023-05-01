from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/class/(?P<class_code>\w+)/$', consumers.ClassChatConsumer.as_asgi())
]