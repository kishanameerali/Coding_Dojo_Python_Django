from django.shortcuts import render, redirect, HttpResponse
from ..users.models import User

def dash(request):
    db = User.objects.all()
    return render(request, 'dashboard/dash_normal.html', {'all_users': db})

def dash_admin(request):
    current_user = User.objects.get(id=request.session['id'])
    if current_user.user_level == 9:
        db = User.objects.all()
        return render(request, 'dashboard/dash_admin.html', {'all_users': db})
    else:
        return HttpResponse(request, "You are not authorized")

