from settings import PROJECT_PATH
from emergent.base import render
import os

@render("index")
def index(request):
    import random
    price = random.randint(0, 99)
    return {"price": price}

@render("status")
def status(request):
    with open(os.path.join(PROJECT_PATH, "status.txt")) as f:
        status = f.read();
    return {"status": status}
    
