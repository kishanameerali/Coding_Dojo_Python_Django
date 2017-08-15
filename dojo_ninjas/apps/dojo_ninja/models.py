from __future__ import unicode_literals

from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)

    def __str__(self):
        return 'Name: {}, City: {}, State: {}'.format(self.name, self.city, self.state)

class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(Dojo)

    def __str__(self):
        return 'First Name: {} Last Name: {}'.format(self.first_name, self.last_name)


# Create your models here.
