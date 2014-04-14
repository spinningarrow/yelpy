from django.db import models
from django import forms
from django.forms import ModelForm
import json

class Food(models.Model):
    # id = models.CharField(primary_key =True, max_length = 235)
    fb_id = models.CharField(primary_key=True, max_length=235)
    chinese = models.BooleanField()
    indian = models.BooleanField()
    vietnamese = models.BooleanField()
    thai = models.BooleanField()
    western = models.BooleanField()

    # On Python 3: def __str__(self):
    def __unicode__(self):
        return self.chinese

class User(models.Model):
    id = models.CharField(primary_key =True, max_length = 235)
    name = models.CharField(max_length = 255)

    # def __unicode__(self):
    #   return self.name

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
