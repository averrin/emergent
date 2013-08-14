# -*- coding: utf-8 -*-

import os
import random
from django.conf import settings
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


class StatusView(LoginRequiredMixin, TemplateView):
    template_name = 'emergent/status.html'

    def get_context_data(self, **kwargs):
        context = super(StatusView, self).get_context_data(**kwargs)
        with open(os.path.join(settings.PROJECT_PATH, "status.txt")) as f:
            context['status'] = f.read()
        return context


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'emergent/profile.html'


class MyProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'emergent/profile.html'
