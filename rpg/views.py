# Create your views here.from datetime import datetime
from django.views.generic import View
from braces.views import AjaxResponseMixin, JSONResponseMixin
import random
from django.contrib.auth import get_user_model
from activity.models import Event
from rpg.models import Title
from emergent.websockets import Pusher
from datetime import datetime


class AddCoin(JSONResponseMixin, AjaxResponseMixin, View):
    def get_ajax(self, request, *args, **kwargs):
        amount = random.randint(1, 100)
        self.request.user.credits += amount
        self.request.user.save()
        json_dict = {
            'credits': self.request.user.credits,
        }
        msg = {
            "type": "rpg",
            "user": self.request.user.username,
            "message": "<strong><a href='/users/%s'>%s</a></strong> get %s coins for fun" % (
                self.request.user.username,
                self.request.user.username,
                amount
            )
        }
        Event(timestamp=datetime.now(), user=self.request.user, type=msg['type'], message=msg['message']).save()
        Pusher.send("activity", "my_event", msg)
        return self.render_json_response(json_dict)


class AddExp(JSONResponseMixin, AjaxResponseMixin, View):
    def get_ajax(self, request, *args, **kwargs):
        amount = random.randint(1, 100)
        self.request.user.exp += amount
        self.request.user.save()
        json_dict = {
            'exp': self.request.user.exp,
        }
        msg = {
            "type": "rpg",
            "user": self.request.user.username,
            "message": "<strong><a href='/users/%s'>%s</a></strong> get %s XP for fun" % (
                self.request.user.username,
                self.request.user.username,
                amount
            )
        }
        Event(timestamp=datetime.now(), user=self.request.user, type=msg['type'], message=msg['message']).save()
        Pusher.send("activity", "my_event", msg)
        return self.render_json_response(json_dict)


class GiveCoin(JSONResponseMixin, AjaxResponseMixin, View):
    def get_ajax(self, request, *args, **kwargs):
        if self.request.user.credits:
            target_user = get_user_model().objects.get(username=kwargs['username'])
            target_user.credits += 1
            target_user.save()
            self.request.user.credits -= 1
            self.request.user.save()
            json_dict = {
                'success': True,
                'my': self.request.user.credits,
                'new': target_user.credits
            }
        else:
            json_dict = {
                'success': False,
                'reason': "No money"
            }

        return self.render_json_response(json_dict)


class BuyView(JSONResponseMixin, AjaxResponseMixin, View):
    def get_ajax(self, request, *args, **kwargs):
        if kwargs["item"] == "cheater" and self.request.user.credits >= 5:
            self.request.user.credits -= 5
            self.request.user.titles.add(Title.objects.get(name="Cheater"))
            self.request.user.save()
            json_dict = {
                'success': True,
                'coins': self.request.user.credits
            }
        else:
            json_dict = {
                'success': False,
                'reason': "No money"
            }
        return self.render_json_response(json_dict)
