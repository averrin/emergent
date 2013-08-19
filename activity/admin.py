from django.contrib import admin
from django.contrib.auth import get_user_model
from models import Event


class EventAdmin(admin.ModelAdmin):
    class Meta():
        model = Event
    #fields = ("timestamp", "user", 'type', 'message')
    list_display = ("timestamp", "user", 'type', 'message')

admin.site.register(Event, EventAdmin)
