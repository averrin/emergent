import pusher
from django.conf import settings


class PusherWrapper(object):

    def __init__(self):

        self.p = pusher.Pusher(
            app_id=settings.PUSHER_APPID,
            key=settings.PUSHER_KEY,
            secret=settings.PUSHER_SECRET
        )

    def send(self, channel, event, msg):
        self.p[channel].trigger(event, msg)

Pusher = PusherWrapper()
