from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, 'store/index.html')

def buy(request):
    request.session['quantity'] = int(request.POST['quantity'])
    
    if request.POST['product_id'] == 1:
        price = 19.99
        request.session['purchase'] = price * request.session['quantity']
    elif request.POST['product_id'] == 2:
        price = 29.99
        purchase = price * request.session['quantity']
    elif request.POST['product_id'] == 3:
        price = 4.99
        purchase = price * request.session['quantity']
    elif request.POST['product_id'] == 4:
        price = 49.99
        purchase = price * request.session['quantity']

    try:
        request.session['items_ordered']
    except KeyError:
        request.session['items_ordered'] = 0
    
    try:
        request.session['total_purchases']
    except KeyError:
        request.session['total_purchases'] = 0
    
    request.session['items_ordered'] += request.session['quantity']
    request.session['total_purchases'] += purchase
    return redirect('/checkout')

def checkout(request):
    return render(request, 'store/checkout.html')
