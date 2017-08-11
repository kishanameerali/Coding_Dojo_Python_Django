from django.shortcuts import render, HttpResponse, redirect
import random
import datetime
from datetime import date

def index(request):
    try:
        request.session['word_total']
    except KeyError:
        request.session['word_total'] = []
    return render(request, 'words_session/index.html')

def process(request):
    request.session['word'] = request.POST['word']
    request.session['color'] = request.POST['color']
    try:
        request.POST['font_size']
        request.session['font_size'] = True
        request.session['font'] = '2em'
    except:
        request.session['font_size'] = False
        request.session['font'] = '1em'
    request.session['word_total'].insert(0, request.session['word'] + ' added on ' + datetime.datetime.now().strftime('%Y/%m/%d %I:%M'))
    return redirect('/')

def reset(request):
    del request.session['word_total']
    return redirect('/')
