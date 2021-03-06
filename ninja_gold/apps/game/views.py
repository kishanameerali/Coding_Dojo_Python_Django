from django.shortcuts import render, HttpResponse, redirect
import random
import datetime
from datetime import date

def index(request):
    try:
        request.session['gold_total']
    except KeyError:
        request.session['gold_total'] = 0
    
    try:
        request.session['result']
    except KeyError:
        request.session['result'] = []
    
    return render(request, 'game/index.html')

def process_money(request):
    if request.POST['building'] == 'farm':
        gold = random.randint(10,21)
        request.session['gold_total'] += gold
        earnings = "Earned " + str(gold) + " from the farm! (" + datetime.datetime.now().strftime('%Y/%m/%d %I:%M') + ")"
        earnings_tuple = (earnings, 'green')
        request.session['result'].insert(0,earnings_tuple)
        print gold
        print request.session['gold_total']
    elif request.POST['building'] == 'cave':
        gold = random.randint(5,11)
        request.session['gold_total'] += gold
        earnings = "Earned " + str(gold) + " from the cave! (" + datetime.datetime.now().strftime('%Y/%m/%d %I:%M') + ")"
        earnings_tuple = (earnings, 'green')
        request.session['result'].insert(0,earnings_tuple)
        print gold
        print request.session['gold_total']
    elif request.POST['building'] == 'house':
        gold = random.randint(2,5)
        request.session['gold_total'] += gold
        earnings = "Earned " + str(gold) + " from the house! (" + datetime.datetime.now().strftime('%Y/%m/%d %I:%M') + ")"
        earnings_tuple = (earnings, 'green')
        request.session['result'].insert(0,earnings_tuple)
        print gold
        print request.session['gold_total']
    elif request.POST['building'] == 'casino':
        gold = random.randint(-50,51)
        request.session['gold_total'] += gold
        if gold > 0:
            earnings = "Entered a casino and won " + str(gold) + "... YAYYY! (" + datetime.datetime.now().strftime('%Y/%m/%d %I:%M') + ")"
            earnings_tuple = (earnings, 'green')
            request.session['result'].insert(0,earnings_tuple)
        else:
            earnings = "Entered a casino and lost " + str(gold*(-1)) + "... Ouch! (" + datetime.datetime.now().strftime('%Y/%m/%d %I:%M') + ")"
            earnings_tuple = (earnings, 'red')
            request.session['result'].insert(0,earnings_tuple)
        print gold
        print request.session['gold_total']
    return redirect('/')
