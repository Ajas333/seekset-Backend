"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from chat.route import websocket_urlpatterns
from channels.auth import AuthMiddlewareStack

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
# django.setup()

application = get_asgi_application()

application = ProtocolTypeRouter({
    "http":application,
    "websocket":AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)
    )
})
