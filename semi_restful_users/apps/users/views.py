from django.shortcuts import render, redirect, HttpResponse
from .models import Enduser
from django.contrib import messages

def index(request):
    db = Enduser.objects.all()
    return render(request, 'users/index.html', {'all_users': db})

def add_user(request):
    return render(request, 'users/add_user.html')

def create(request):
    validations = Enduser.objects.validator(request.POST)
    if len(validations) == 0:
        user = Enduser(
            full_name = request.POST['full_name'],
            email = request.POST['email']
        )
        user.save()
        id = user.id
        return redirect('/users/'+str(id))
    else:
        for error in validations:
            messages.add_message(request, messages.INFO, error)
        return redirect('/users/new')


def user_info(request, id):
    if request.method == 'POST':
        user = Enduser.objects.get(id=id)
        user.full_name = request.POST['full_name']
        user.email = request.POST['email']
        user.save()
        return redirect('/users/'+id)
    else:
        user = Enduser.objects.get(id=id)
        return render(request, 'users/show_user.html', {'user': user})

def edit_user(request, id):
    user = Enduser.objects.get(id=id)
    return render(request, 'users/edit_user.html', {'user': user})

def destroy_user(request, id):
    user = Enduser.objects.get(id=id)
    user.delete()
    return redirect('/users')


# Create your views here.
