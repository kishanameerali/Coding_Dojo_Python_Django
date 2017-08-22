from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'users/index.html')

def success(request):
    return render(request, 'users/success.html')

def register(request):
    validations = User.objects.validator(request.POST)
    if len(validations) == 0:
        new_user = User.objects.create_user(request.POST)
        request.session['id'] = new_user.id
        messages.success(request, "Success, Welcome {}, successfully registered".format(new_user.first_name))
        return redirect('/success')
    else:
        for errors in validations:
            messages.error(request, errors)
        return redirect('/')

def login(request):
    user_login = User.objects.filter(email=request.POST['email'])
    if len(user_login) > 0:
        if bcrypt.checkpw((request.POST['password']).encode(), (user_login[0].password).encode()):
            request.session['id'] = user_login[0].id
            print user_login[0].first_name
            messages.success(request, "Success, Welcome {}, successfully logged in".format(user_login[0].first_name))
            return redirect('/success')
        else:
            messages.error(request, "Email or Password Invalid")
            return redirect('/')
    else:
        messages.error(request, "Email or Password Invalid")
        return redirect('/')


