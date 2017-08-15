from __future__ import unicode_literals

from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField

    def __str__(self):
        return 'Name: {}, City: {}, State: {}, Desc: {}'.format(self.name, self.city, self.state, self.desc)

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(Dojo)

    def __str__(self):
        return 'First Name: {} Last Name: {}'.format(self.first_name, self.last_name)

class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return 'Name: {}, Desc: {}'.format(self.name, self.desc)

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    notes = models.TextField
    books = models.ManyToManyField(Book)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return 'First Name: {}, Last Name {}, Email: {}, Notes: {}'.format(self.first_name, self.last_name, self.email, self.notes)
