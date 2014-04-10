from django.forms import ModelForm
from polls.models import Author


class AuthorForm(ModelForm):
	class Meta:
		model = Author
		fields = ['name', 'title']
	def process(self):
		cd = self.cleaned_data
		print cd['name']

