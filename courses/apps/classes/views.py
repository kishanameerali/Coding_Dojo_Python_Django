from django.shortcuts import render, redirect
from .models import Course
from django.contrib import messages

def index(request):
    courses = Course.objects.all()
    return render(request, 'classes/index.html', {'all_courses': courses})

def add_course(request):
    validations = Course.objects.validator(request.POST)
    if len(validations) == 0:
        new_course = Course(
            name = request.POST['name'],
            desc = request.POST['desc']
        )
        new_course.save()
        print new_course
    else:
        for error in validations:
            messages.add_message(request, messages.INFO, error)
    return redirect('/')

def destroy(request, id):
    del_course = Course.objects.get(id=id)
    return render(request, 'classes/destroy.html', {'del_course': del_course})

def confirm_destroy(request, id):
    del_course = Course.objects.get(id=id)
    del_course.delete()
    return redirect('/')

# Create your views here.
