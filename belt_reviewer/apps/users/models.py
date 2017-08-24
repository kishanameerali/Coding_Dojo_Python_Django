from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = []
        #to check if email already has been registered
        if self.filter(email=postData['email']):
            errors.append("Email has already been registered")
        #to check if alias is already taken
        if self.filter(email=postData['alias']):
            errors.append("That Alias is already in use")
        if len(postData['name']) < 2:
            errors.append("Name must be 2 characters minimum")
        if len(postData['alias']) < 2:
            errors.append("Alias must be 2 characters minimum")
        if not EMAIL_REGEX.match(postData['email']):
            errors.append("Invalid Email Address")
        if len(postData['password']) < 8:
            errors.append("Password must be 8 chracters minimum")
        if postData['password'] != postData['confirm_password']:
            errors.append("Password and confirmation don't match")
        return errors

    def create_user(self, clean_data):
        hashed_pw = bcrypt.hashpw(clean_data['password'].encode(), bcrypt.gensalt())
        return self.create(
            name = clean_data['name'],
            alias = clean_data['alias'],
            email = clean_data['email'],
            password = hashed_pw
        )

    def login_validator(self, post_data):
        #returns tuple ([errors], <User> or None)
        errors = []
        user_login = None
        if not self.filter(email=post_data['email']):
            errors.append("Email or Password Invalid")
        else:
            user_login = self.get(email=post_data['email'])
            if not bcrypt.checkpw(post_data['password'].encode(), user_login.password.encode()):
                errors.append("Email or Password Invalid")
                user_login = None
        return (errors, user_login)

class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=254, unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return "Name: {}, Alias: {}, Email: {}".format(self.name, self.alias, self.email)
