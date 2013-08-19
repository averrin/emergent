from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model


class Event(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    type = models.TextField(choices=(
        ("chat", "Chat"), ("other", "Other"))
    )
    message = models.TextField()
    user = models.ForeignKey(get_user_model())