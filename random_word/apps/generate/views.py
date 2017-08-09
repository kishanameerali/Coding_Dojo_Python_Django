from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
import random
import string

def index(request):
    try:
        request.session['counter']
    except KeyError:
        request.session['counter'] = 0
    return render(request, 'generate/index.html')

def random_word(request):
    request.session['counter'] += 1
    request.session['word'] = get_random_string(length=14)
    return render(request, 'generate/index.html')

def reset(request):
    del request.session['counter']
    return redirect('/')
