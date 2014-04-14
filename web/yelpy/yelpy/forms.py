from django.forms import ModelForm
from yelpy.models import Food


class FoodForm(ModelForm):
	class Meta:
		model = Food
		fields = ['chinese', 'indian','vietnamese','thai','western']
	def process(self):
		cd = self.cleaned_data
		print cd['chinese']

