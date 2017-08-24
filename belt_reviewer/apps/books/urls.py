from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.books_index),
    url(r'^add$', views.add),
    url(r'^create_new_review$', views.create_new_review),
    url(r'^create_review/(?P<id>\d+)$', views.create_review),
    url(r'^delete/(?P<id>\d+)$', views.delete_review),
    url(r'^(?P<id>\d+)$', views.book_info)
]