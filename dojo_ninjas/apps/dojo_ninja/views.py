from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return HttpResponse("I'm just here to make models")

# Create your views here.
