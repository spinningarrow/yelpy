from django.db import models
from django.forms import ModelForm

class Food(models.Model):
	chinese = models.BooleanField()
	indian = models.BooleanField()	
	vietnamese = models.BooleanField()	
	thai = models.BooleanField()	
	western = models.BooleanField()	

	# On Python 3: def __str__(self):
	def __unicode__(self):
		return self.chinese