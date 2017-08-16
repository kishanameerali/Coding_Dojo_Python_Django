from __future__ import unicode_literals
from django.db import models

class CourseManager(models.Manager):
    def validator(self, postData):
        errors = []
        if len(postData['name']) < 6:
            errors.append('Course name must be more than 5 characters')
        if len(postData['desc']) < 16:
            errors.append('Description must be more than 15 characters')
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()

    def __str__(self):
        return 'Name: {}, Description: {}, Created at: {}'.format(self.name, self.desc, self.created_at)

# Create your models here.
