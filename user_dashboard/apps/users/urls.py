from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^signin$', views.signin),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^process$', views.process),
    url(r'^users/new$', views.new),
    url(r'^users/add_new$', views.add_new),
    url(r'^users/edit$', views.edit),
    url(r'^users/edit_info$', views.edit_info),
    url(r'^users/edit_pw$', views.edit_pw),
    url(r'^users/edit_desc$', views.edit_desc),
    url(r'^users/edit/(?P<id>\d+)$', views.edit_user),
    url(r'^users/edit/edit_id_info$', views.edit_id_info),
    url(r'^users/edit/edit_id_pw$', views.edit_id_pw),
    url(r'^users/show/(?P<id>\d+)$', views.message_board),
    url(r'^users/show/message$', views.leave_message),
    url(r'^users/show/comment$', views.leave_comment),
]