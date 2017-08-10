from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'surveys/index.html')

def process(request):
    try:
        request.session['counter']
    except KeyError:
        request.session['counter'] = 0
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    request.session['counter'] += 1
    return redirect('/result')

def results(request):
    return render(request, 'surveys/result.html')

# Create your views here.
