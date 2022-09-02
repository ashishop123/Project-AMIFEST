from django.db import models
from django.db.models import manager
from django.db.models.fields import BLANK_CHOICE_DASH


# Create your models here.


class event(models.Model):
    name = models.CharField('event name', max_length=122)
    date = models.DateField('event date')
    venue = models.CharField(max_length=120)
    block = models.CharField('block name', max_length=120)
    manager = models.CharField('manager name', max_length=120)
    description = models.TextField(blank=True )
    image = models.ImageField(blank = True)

    def __str__(self):
        return self.name

class user_registration(models.Model):
    first_name = models.CharField('first_name', max_length=122, blank=False)
    last_name = models.CharField('last_name', max_length=122, blank=False)
    email = models.EmailField('email', max_length=125)
    block = models.CharField('block name', max_length=120)
    branch = models.CharField('branch', max_length=120)
    phone_number = models.CharField('phone_number', max_length=10)
    university = models.CharField(max_length=150)

    def __str__(self):
        return self.first_name
