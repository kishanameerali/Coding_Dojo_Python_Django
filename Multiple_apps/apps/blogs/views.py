from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    response = "placeholder to display all the list of blogs"
    return HttpResponse(response)

def create(request):
    return redirect ('/')

def show(request, number):
    response = "placeholder to display blog " + number
    return HttpResponse(response)

def edit(request, number):
    response = "placeholder to edit blog " + number
    return HttpResponse(response)

def destroy(request, number):
    return redirect('/')