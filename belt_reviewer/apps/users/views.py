from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import User
from ..books.models import Book, Review
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'users/index.html')

def register(request):
    validations = User.objects.register_validator(request.POST)
    if len(validations) == 0:
        new_user = User.objects.create_user(request.POST)
        request.session['id'] = new_user.id
        messages.success(request, "Welcome {}!".format(new_user.alias))
        return redirect('/books')
    else:
        for errors in validations:
            messages.error(request, errors)
        return redirect('/')

def login(request):
    login_result = User.objects.login_validator(request.POST)
    if login_result[0]:
        for error in login_result[0]:
            messages.error(request, error)
        return redirect('/')
    else:
        request.session['id'] = login_result[1].id
        messages.success(request, "Welcome {}!".format(login_result[1].alias))
        return redirect('/books')

def user_info(request, id):
    the_user = User.objects.get(id=id)
    reviews = the_user.reviews.all()
    #books = []
    #for book in reviews:
        #books.append(Book.objects.get(id=reviews.reviewer.id))
    return render(request, 'users/user_info.html', {'user': the_user, 'reviews': reviews})

def logout(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')