from settings import PROJECT_PATH
from emergent.base import render
import os

@render("status")
def status(request):
    with open(os.path.join(PROJECT_PATH, "status.txt")) as f:
        status = f.read();
    return {"status": status}
    
