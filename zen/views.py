# -*- coding: utf-8 -*-

from random import choice

from django.views.generic import TemplateView

from utils import yodaize
from zen_lines import MESSAGE


__all__ = (
    'IndexView',
)


class IndexView(TemplateView):
    template_name = 'zen/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['message'] = yodaize(choice(MESSAGE))
