from django.db import models
from django import forms
from django.forms import ModelForm
import json

class All(models.Model):
    # class Meta:
    #     select_on_save = True

    id = models.CharField(primary_key=True, max_length=235)
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
        return "sdss"

    @staticmethod
    def category_dict():
        return {
            'chinese': 'food',
            'indian': 'food',
            'vietnamese': 'food',
            'thai': 'food',
            'western': 'food',

            'fitness': 'sports',
            'golf': 'sports',
            'football': 'sports',
            'swimming': 'sports',
            'fishing': 'sports',

            'clothes': 'shops',
            'accessories': 'shops',
            'women': 'shops',
            'children': 'shops',
            'men': 'shops',
            'gifts': 'shops',

            'gallery': 'arts',
            'cinema': 'arts',
            'theater': 'arts',
        }

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
