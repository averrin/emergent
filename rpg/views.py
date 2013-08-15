# Create your views here.
from django.views.generic import View
from braces.views import AjaxResponseMixin, JSONResponseMixin
import random
from django.contrib.auth import get_user_model


class AddCoin(JSONResponseMixin, AjaxResponseMixin, View):
    def get_ajax(self, request, *args, **kwargs):
        self.request.user.credits += random.randint(1, 100)
        self.request.user.save()
        json_dict = {
            'credits': self.request.user.credits,
        }
        return self.render_json_response(json_dict)


class AddExp(JSONResponseMixin, AjaxResponseMixin, View):
    def get_ajax(self, request, *args, **kwargs):
        self.request.user.exp += random.randint(1, 100)
        self.request.user.save()
        json_dict = {
            'exp': self.request.user.exp,
        }
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
            }

        return self.render_json_response(json_dict)
