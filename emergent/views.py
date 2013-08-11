from settings import PROJECT_PATH
from emergent.base import render
from django.contrib.auth.decorators import login_required
import os

@render("emergent/index")
def index(request):
    import random
    price = random.randint(0, 99)
    return {"price": price}

@login_required
@render("emergent/status")
def status(request):
    with open(os.path.join(PROJECT_PATH, "status.txt")) as f:
        status = f.read();
    return {"status": status}
    
