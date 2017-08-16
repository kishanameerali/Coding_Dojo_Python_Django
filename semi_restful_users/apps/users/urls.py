from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^users$', views.index),
    url(r'^users/new$', views.add_user),
    url(r'^users/create$', views.create),
    url(r'^users/(?P<id>\d+)$', views.user_info),
    url(r'^users/(?P<id>\d+)/edit$', views.edit_user),
    url(r'^users/(?P<id>\d+)/destroy$', views.destroy_user)
]