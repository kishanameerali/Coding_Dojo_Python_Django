from django.shortcuts import render, redirect, HttpResponse

def index(request):
    render(request, 'user_login/index.html')

# Create your views here.
