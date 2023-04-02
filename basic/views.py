from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Pooja")

# Create your views here.
