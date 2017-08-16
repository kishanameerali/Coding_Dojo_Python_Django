from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses/add_course$', views.add_course),
    url(r'^courses/destroy/(?P<id>\d+)$', views.destroy),
    url(r'^courses/confirm_destroy/(?P<id>\d+)$', views.confirm_destroy)
]