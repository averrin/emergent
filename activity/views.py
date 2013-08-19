# Create your views here.

import os
import random
from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.views.generic import TemplateView, View
from braces.views import LoginRequiredMixin, JSONResponseMixin, AjaxResponseMixin
import misaka as m


__all__ = (
    'StreamView',
    'ChatSendView'
)



class StreamView(LoginRequiredMixin, TemplateView):
    template_name = 'activity/stream.html'

    def get_context_data(self, **kwargs):
        context = super(StreamView, self).get_context_data(**kwargs)
        return context


class ChatSendView(LoginRequiredMixin, JSONResponseMixin, AjaxResponseMixin, View):
    def post_ajax(self, request, *args, **kwargs):
        import pusher

        p = pusher.Pusher(
            app_id=settings.PUSHER_APPID,
            key=settings.PUSHER_KEY,
            secret=settings.PUSHER_SECRET
        )
        p['activity'].trigger('my_event', {
            'message': m.html(self.request.POST['message']),
            'user': self.request.user.username,
            'type': 'chat',
        })
        json_dict = {
            "success": True
        }
        return self.render_json_response(json_dict)


