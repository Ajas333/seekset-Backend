from django.urls import path
from .consumers import ChatConsumer,NotificationConsumer

websocket_urlpatterns = [
    path('ws/chat/<int:candidate_id>/<int:employer_id>/<int:user_id>', ChatConsumer.as_asgi()),
    path('ws/notifications/<int:user_id>/', NotificationConsumer.as_asgi()),
]