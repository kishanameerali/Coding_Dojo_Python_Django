from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, 'store/index.html')

def buy(request):
    request.session['quantity'] = int(request.POST['quantity'])

    try:
        request.session['purchase']
    except KeyError:
        request.session['purchase'] = 0

    try:
        request.session['price']
    except KeyError:
        request.session['price'] = 0
    
    if request.POST['product_id'] == 1:
        request.session['price'] = 19.99
    elif request.POST['product_id'] == 2:
        request.session['price'] = 29.99
    elif request.POST['product_id'] == 3:
        request.session['price'] = 4.99
    elif request.POST['product_id'] == 4:
        request.session['price'] = 49.99

    request.session['purchase'] = request.session['price'] * request.session['quantity']

    try:
        request.session['items_ordered']
    except KeyError:
        request.session['items_ordered'] = 0
    
    try:
        request.session['total_purchases']
    except KeyError:
        request.session['total_purchases'] = 0
    
    request.session['items_ordered'] += request.session['quantity']
    request.session['total_purchases'] += request.session['purchase']
    return redirect('/checkout')

def checkout(request):
    return render(request, 'store/checkout.html')
