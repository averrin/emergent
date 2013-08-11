# -*- coding: utf-8 -*-

import os

from django.conf import settings

from emergent.base import render


__all__ = (
    'index',
    'status',
)


@render("emergent/index")
def index(request):
    import random
    price = random.randint(0, 99)
    return {"price": price}


@render("emergent/status")
def status(request):
    with open(os.path.join(settings.PROJECT_PATH, "status.txt")) as f:
        status = f.read()
    return {"status": status}
