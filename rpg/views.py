# Create your views here.
from django.views.generic import View
from braces.views import AjaxResponseMixin, JSONResponseMixin
import random


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
