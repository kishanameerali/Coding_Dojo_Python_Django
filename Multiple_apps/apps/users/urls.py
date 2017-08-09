from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.users),
    url(r'^login/$', views.login),
    url(r'^new/$', views.register),
    url(r'^register/$', views.register)
]