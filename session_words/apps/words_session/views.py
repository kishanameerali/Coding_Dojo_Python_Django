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
    word = request.POST['word']
    color = request.POST['color']
    try:
        request.POST['font_size']
        request.session['font_size'] = True
        font = '2em'
    except:
        request.session['font_size'] = False
        font = '1em'
    date_added = datetime.datetime.now().strftime('%Y/%m/%d %I:%M')
    word_tuple = (word, color, font, date_added)
    print word_tuple[0]
    request.session['word_total'].insert(0, word_tuple)
    print request.session['word_total'][0][1]
    return redirect('/')

def reset(request):
    del request.session['word_total']
    return redirect('/')
