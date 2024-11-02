from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello World, you are at the wordle landing page!")
# Create your views here.
