from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, 'store/index.html')

def buy(request):
    request.session['quantity'] = request.POST['quantity']
    items_ordered = 0
    total_purchases = 0
    if request.POST['product_id'] == 1:
        price = 19.99
        purchase = price * request.session['quantity']
        items_ordered += 1
        total_purchases += purchase
    elif request.POST['product_id'] == 2:
        price = 29.99
        purchase = price * request.session['quantity']
        items_ordered += 1
        total_purchases += purchase
    elif request.POST['product_id'] == 3:
        price = 4.99
        purchase = price * request.session['quantity']
        items_ordered += 1
        total_purchases += purchase
    elif request.POST['product_id'] == 4:
        price = 49.99
        purchase = price * request.session['quantity']
        items_ordered += 1
        total_purchases += purchase
    return redirect('/checkout')

def checkout(request):
    return render(request, 'store/checkout.html')
