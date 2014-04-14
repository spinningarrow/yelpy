from django.forms import ModelForm
from yelpy.models import All
from django import forms


class AllForm(ModelForm):
    class Meta:
        model = All
        fields = ['chinese', 'indian','vietnamese','thai','western','fitness','golf','football','swimming','fishing','clothes','accessories','women','children','men','gifts','gallery','cinema','theater','fb_id']
        # exclude = ['id']
    def process(self):
        cd = self.cleaned_data
        print cd['chinese']
    def __init__(self, *args, **kwargs):
        super(AllForm, self).__init__(*args, **kwargs)
        self.fields['fb_id'].widget = forms.HiddenInput()

