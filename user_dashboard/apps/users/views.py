from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import User, Message, Comment
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'users/index.html')

def signin(request):
    return render(request, 'users/signin.html')

def register(request):
    return render(request, 'users/register.html')

def process(request):
    validations = User.objects.validator(request.POST)
    if len(validations) == 0:
        new_user = User.objects.create_user(request.POST)
        if new_user.user_level == 9:
            request.session['id'] = new_user.id
            return redirect('/dashboard/admin')          
        else:
            request.session['id'] = new_user.id
            return redirect('/dashboard')
    else:
        for errors in validations:
            messages.error(request, errors)
        return redirect('/register')

def login(request):
    user_login = User.objects.filter(email=request.POST['email'])
    if len(user_login) == 0:
        messages.error(request, "Email or Password Invalid")
        return redirect('/signin')
    elif bcrypt.checkpw((request.POST['password']).encode(), (user_login[0].password).encode()):
        request.session['id'] = user_login[0].id
        print user_login[0].first_name
        if user_login[0].user_level == 9:
            return redirect('/dashboard/admin')
        else:
            return redirect('/dashboard')

def edit(request):
    return render(request, 'users/edit.html')

def edit_info(request):
    validations = User.objects.validator(request.POST)
    if len(validations) == 0:
        new_info = User.objects.get(id=request.session['id'])
        new_info.email = request.POST['email']
        new_info.first_name = request.POST['first_name']
        new_info.last_name = request.POST['last_name']
        new_info.save()
        return redirect('/dashboard')
    else:
        for errors in validations:
            messages.error(request, errors)
        return redirect('/users/new')

def edit_pw(request):
    validations = User.objects.validator(request.POST)
    if len(validations) == 0:
        new_info = User.objects.get(id=request.session['id'])
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        new_info.password = hashed_pw
        new_info.save()
        return redirect('/dashboard')
    else:
        for errors in validations:
            messages.error(request, errors)
        return redirect('/users/new')

def edit_desc(request):
    validations = User.objects.validator(request.POST)
    if len(validations) == 0:
        new_info = User.objects.get(id=request.session['id'])
        new_info.desc = request.POST['desc']
        new_info.save()
        return redirect('/dashboard')
    else:
        for errors in validations:
            messages.error(request, errors)
        return redirect('/users/new')

def new(request):
    valid_user = User.objects.get(id=request.session['id'])
    if valid_user.user_level == 9:
        return render(request, 'users/add_new.html')
    else:
        return HttpResponse(request, "You are not authorized for this URL")

def add_new(request):
    validations = User.objects.validator(request.POST)
    if len(validations) == 0:
        new_user = User.objects.create_user(request.POST)
        return redirect('/dashboard/admin')
    else:
        for errors in validations:
            messages.error(request, errors)
        return redirect('/users/new')

def edit_user(request, id):
    user_edit = User.objects.get(id=id)
    return render(request, 'users/edit_user.html', {'user': user_edit})

def edit_id_info(request, id):
    validations = User.objects.validator(request.POST)
    if len(validations) == 0:
        user_edit = User.objects.get(id=id)
        user_edit.email = request.POST['email']
        user_edit.first_name = request.POST['first_name']
        user_edit.last_name = request.POST['last_name']
        user_edit.user_level = request.POST['user_level']
        user_edit.save()
        return redirect('/dashboard/admin')
    else:
        for errors in validations:
            messages.error(request, errors)
        return redirect('/edit_user')

def edit_id_pw(request, id):
    validations = User.objects.validator(request.POST)
    if len(validations) == 0:
        user_edit = User.objects.get(id=id)
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user_edit.password = hashed_pw
        user_edit.save()
        return redirect('/dashboard/admin')
    else:
        for errors in validations:
            messages.error(request, errors)
        return redirect('/edit_user')

def message_board(request, id):
    show_user = User.objects.get(id=id)
    msgs = Message.objects.filter(to_user=show_user.id)
    comms = Comment.objects.all()
    return render(request, 'users/show_user.html', {'user': show_user, 'all_msgs': msgs, 'all_comms': comms})

def leave_message(request, id):
    show_user = User.objects.get(id=id)
    validations = Message.objects.validator(request.POST)
    if len(validations) == 0:
        new_message = Message.objects.create_message(request.POST)
    else:
        for errors in validations:
            messages.error(request, errors)
        return redirect('/message_board')

def leave_comment(request, id):
    show_user = User.objects.get(id=id)
    validations = Comment.objects.validator(request.POST)
    if len(validations) == 0:
        message_id = request.POST['chosen_msg']
        show_message = Message.objects.get(id=message_id)
        new_comment = Comment.objects.create_comment(request.POST)
    else:
        for errors in validations:
            messages.error(request, errors)
        return redirect('/message_board')


