from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, 'store/index.html')

def buy(request):
    if "purchase_price" in request.session.keys():
        del request.session['purchase_price']

    price = 0

    if request.POST['product_id'] == 1:
        price = 19.99 * int(request.POST['quantity'])
        #purchase = price * int(request.POST['quantity'])
    elif request.POST['product_id'] == 2:
        price = 29.99 * int(request.POST['quantity'])
        #purchase = price * int(request.POST['quantity'])
    elif request.POST['product_id'] == 3:
        price = 4.99 * int(request.POST['quantity'])
        #purchase = price * int(request.POST['quantity'])
    elif request.POST['product_id'] == 4:
        price = 49.99 * int(request.POST['quantity'])
        #purchase = price * int(request.POST['quantity'])

    try:
        request.session['items_ordered']
    except KeyError:
        request.session['items_ordered'] = 0
    
    try:
        request.session['total_purchases']
    except KeyError:
        request.session['total_purchases'] = 0

    request.session['total_purchases'] += price
    request.session['items_ordered'] += int(request.POST['quantity'])
    request.session['purchase_price'] = price
    
    print request.session['purchase']
    print request.session['items_ordered']
    print request.session['total_purchases']
    return redirect('/checkout')

def checkout(request):
    return render(request, 'store/checkout.html')
