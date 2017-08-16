from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class User_manager(models.Manager):
    def validator(self, postData):
        errors = []
        if len(postData['full_name']) < 3:
            errors.append('Name must be more than 3 characters')
        if not EMAIL_REGEX.match(postData['email']):
            errors.append('Invalid Email Address')
        return errors

class Enduser(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = User_manager()

    def __str__(self):
        return 'Name: {} Email: {}'.format(self.full_name, self.email)

# Create your models here.
