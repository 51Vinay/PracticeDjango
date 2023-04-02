from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Vinay ❤️ Pooja")

# Create your views here.
