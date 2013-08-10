from django.shortcuts import render
from random import choice
from .utils import yodaize
from .zen import MESSAGE

def index(request):
    message = choice(MESSAGE)
    message = yodaize(message)
    return render(request, 'zen/index.html', {'message': message})
