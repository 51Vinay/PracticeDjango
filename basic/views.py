from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Djeango repo work succesfully")

# Create your views here.
