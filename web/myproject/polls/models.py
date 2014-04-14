from django.db import models
from django.forms import ModelForm


class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.question_text
	def was_published_recently(self):
		return self.pub_date >= TIME_ZONE.now() - datetime.timedelta(days=1)


class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.choice_text

class MyModel(models.Model):
	field1 = models.CharField(max_length=40, blank=False, null=False)
	field2 = models.CharField(max_length=60, blank=True, null=True)

TITLE_CHOICES = (
	('MR', 'Mr.'),
	('MRS', 'Mrs.'),
	('MS', 'Ms.'),
)

class Author(models.Model):
	name = models.CharField(max_length=100)
	title = models.CharField(max_length=3, choices=TITLE_CHOICES)
	
	# On Python 3: def __str__(self):
	def __unicode__(self):
		return self.name	
