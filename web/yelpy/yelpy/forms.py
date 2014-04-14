from django.forms import ModelForm
from yelpy.models import *


class foodForm(ModelForm):
	class Meta:
		model = food
		fields = ['chinese', 'indian','vietnamese','thai','western']
	def process(self):
		cd = self.cleaned_data
		print cd['chinese']

