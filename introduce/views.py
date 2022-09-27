from django.shortcuts import render
from .models import AccessLog


# Create your views here.
def introduce(request):
    new_log = AccessLog()
    new_log.location = 'introduce.html'
    new_log.save()
    return render(request, 'introduce.html')
