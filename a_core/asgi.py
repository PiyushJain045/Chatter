"""
ASGI config for a_core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'a_core.settings')

# Define the default Django ASGI application to handle HTTP requests
django_asgi_app = get_asgi_application()

from a_rtchat import routing

# ProtocolTypeRouter directs requests based on their type (HTTP, WebSocket, etc.)
application = ProtocolTypeRouter({
    "http": django_asgi_app,  # Correctly reference the Django ASGI application for HTTP
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                routing.websocket_urlpatterns
            )
        ),
    ),
})
