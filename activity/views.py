# Create your views here.from datetime import datetime

import os
import random
from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.views.generic import TemplateView, View
from braces.views import LoginRequiredMixin, JSONResponseMixin, AjaxResponseMixin
import misaka as m
from activity.models import Event
from datetime import datetime
from emergent.websockets import Pusher


__all__ = (
    'StreamView',
    'ChatSendView',
    'HistoryView'
)


class StreamView(LoginRequiredMixin, TemplateView):
    template_name = 'activity/stream.html'

    def get_context_data(self, **kwargs):
        context = super(StreamView, self).get_context_data(**kwargs)
        return context


class HistoryView(LoginRequiredMixin, JSONResponseMixin, AjaxResponseMixin, View):
    def get_ajax(self, request, *args, **kwargs):
        history = Event.objects.all().order_by("timestamp")[:10]
        json_dict = {"history": []}
        for event in history:
            json_dict["history"].append({
                'message': m.html(event.message),
                'user': event.user.username,
                'type': event.type,
                'timestamp': event.timestamp
            })
        return self.render_json_response(json_dict)


class ChatSendView(LoginRequiredMixin, JSONResponseMixin, AjaxResponseMixin, View):
    def post_ajax(self, request, *args, **kwargs):
        msg = {
            'message': m.html(self.request.POST['message']),
            'user': self.request.user.username,
            'type': 'chat',
        }
        Event(timestamp=datetime.now(), user=self.request.user, type='chat', message=msg['message']).save()
        Pusher.send("activity", 'my_event', msg)
        json_dict = {
            "success": True
        }
        return self.render_json_response(json_dict)
