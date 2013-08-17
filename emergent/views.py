# -*- coding: utf-8 -*-

import os
import random
from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.views.generic import TemplateView
from braces.views import LoginRequiredMixin


__all__ = (
    'IndexView',
    'StatusView',
    'ProfileView',
    'MyProfileView',
)


class IndexView(TemplateView):
    template_name = 'emergent/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["price"] = random.randint(0, 99)
        return context

class LoginView(TemplateView):
    template_name = 'emergent/login.html'

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', None)
        if self.request.user.is_authenticated():
            return redirect('me')
            
        return context


class StatusView(LoginRequiredMixin, TemplateView):
    template_name = 'emergent/status.html'

    def get_context_data(self, **kwargs):
        context = super(StatusView, self).get_context_data(**kwargs)
        with open(os.path.join(settings.PROJECT_PATH, "status.txt")) as f:
            context['status'] = f.read()
        return context


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'emergent/profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['profile'] = get_user_model().objects.get(username=kwargs['username'])
        return context


class MyProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'emergent/profile.html'

    def get_context_data(self, **kwargs):
        context = super(MyProfileView, self).get_context_data(**kwargs)
        context['profile'] = self.request.user
        return context
