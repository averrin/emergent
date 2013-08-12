# -*- coding: utf-8 -*-

from random import choice

from django.shortcuts import render

from utils import yodaize
from zen_lines import MESSAGE


__all__ = (
    'index',
)


def index(request):
    message = choice(MESSAGE)
    message = yodaize(message)
    return render(request, 'zen/index.html', {'message': message})
