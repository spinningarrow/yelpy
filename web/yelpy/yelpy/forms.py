from django.forms import ModelForm
from yelpy.models import Food
from django import forms


class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields = ['chinese', 'indian','vietnamese','thai','western','fb_id']
        # exclude = ['id']
    def process(self):
        cd = self.cleaned_data
        print cd['chinese']
    def __init__(self, *args, **kwargs):
        super(FoodForm, self).__init__(*args, **kwargs)
        self.fields['fb_id'].widget = forms.HiddenInput()

