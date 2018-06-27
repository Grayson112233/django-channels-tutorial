from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chat.routing

application = ProtocolTypeRouter({
	# HTTP Django views are added by default
	'websocket': AuthMiddlewareStack(
		URLRouter(
			chat.routing.websocket_urls
		)
	),
})