from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UserManager(models.Manager):
    def validator(self, postData):
        errors = []
        if len(postData['first_name']) < 2:
            errors.append("First Name must be 2 characters minimum")
        if (postData['first_name']).isalpha() == False:
            errors.append("First Name can only contain letters")
        if len(postData['last_name']) < 2:
            errors.append("Last Name must be 2 characters minimum")
        if (postData['last_name']).isalpha() == False:
            errors.append("Last Name can only contain letters")
        if not EMAIL_REGEX.match(postData['email']):
            errors.append("Invalid Email Address")
        if len(postData['password']) < 8:
            errors.append("Password must be 8 chracters minimum")
        if postData['password'] != postData['confirm_password']:
            errors.append("Password and confirmation don't match")
        return errors

    def create_user(self, clean_data):
        hashed_pw = bcrypt.hashpw(clean_data['password'].encode(), bcrypt.gensalt())
        if User.objects.count() == 0:
            return self.create(
                first_name = clean_data['first_name'],
                last_name = clean_data['last_name'],
                email = clean_data['email'],
                password = hashed_pw,
                user_level = 9,
            )
        else:
            return self.create(
                first_name = clean_data['first_name'],
                last_name = clean_data['last_name'],
                email = clean_data['email'],
                password = hashed_pw,
                user_level = 1,
            )

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=254, unique=True)
    password = models.CharField(max_length=255)
    user_level = models.PositiveIntegerField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return "First Name: {}, Last Name: {}, Email: {}".format(self.first_name, self.last_name, self.email)

class MessageManager(models.Manager):
    def validator(self, postData):
        errors = []
        if len(postData['content']) < 1:
            errors.append("You gotta put something down, can't be blank")
        return errors

    def create_message(self, clean_data):
        current_user = User.objects.get(id=request.session['id'])
        return self.create(
            content = clean_data['content'],
            to_user = show_user.id,
            from_user_first = current_user.first_name,
            from_user_last = current_user.last_name,
            from_user = current_user.id
        )


class Message(models.Model):
    content = models.TextField()
    from_user_first = models.CharField(max_length=255)
    from_user_last = models.CharField(max_length=255)
    to_user = models.ForeignKey(User, related_name='messages_received')
    from_user = models.ForeignKey(User, related_name='messages_sent')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = MessageManager()

    def __str__(self):
        return "Message: {}, To: {}, From: {}, ".format(self.content, self.to_user, self.from_user)


class CommentManager(models.Manager):
    def validator(self, postData):
        errors = []
        if len(postData['content']) < 1:
            errors.append("You gotta put something down, can't be blank")
        return errors

    def create_comment(self, clean_data):
        current_user = User.objects.get(id=request.session['id'])
        return self.create(
            content = clean_data['content'],
            message = show_message.id,
            from_user_first = current_user.first_name,
            from_user_last = current_user.last_name,
            from_user = current_user.id
        )


class Comment(models.Model):
    content = models.TextField()
    from_user_first = models.CharField(max_length=255)
    from_user_last = models.CharField(max_length=255)
    message = models.ForeignKey(Message, related_name='comments')
    from_user = models.ForeignKey(User, related_name='comments_sent')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CommentManager()

    def __str__(self):
        return "Comment: {}, To: {}, From: {}, ".format(self.content, self.message, self.from_user)

