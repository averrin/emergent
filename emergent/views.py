from settings import PROJECT_PATH
from django.http import HttpResponse
import os

def status(request):
    with open(os.path.join(PROJECT_PATH, "status.txt")) as f:
        status = f.read().split('\n');
    return HttpResponse("<br>".join(status))
    
