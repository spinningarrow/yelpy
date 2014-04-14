from django.db import models
from django import forms
from django.forms import ModelForm
import json

class All(models.Model):
    fb_id = models.CharField(primary_key=True, max_length=235)
    #---food categories---
    chinese = models.BooleanField()
    indian = models.BooleanField()
    vietnamese = models.BooleanField()
    thai = models.BooleanField()
    western = models.BooleanField()

    #---sports categories---
    fitness = models.BooleanField()
    golf = models.BooleanField()
    football = models.BooleanField()
    swimming = models.BooleanField()
    fishing = models.BooleanField()

    #---shop categories---
    clothes = models.BooleanField()
    accessories = models.BooleanField()
    women = models.BooleanField()
    children = models.BooleanField()
    men = models.BooleanField()
    gifts = models.BooleanField()

    #---arts categories---
    gallery = models.BooleanField()
    cinema = models.BooleanField()
    theater = models.BooleanField()
    


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
