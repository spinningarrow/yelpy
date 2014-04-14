__author__ = 'user'

from django import forms
from haystack.forms import SearchForm

class ListingSearchForm(SearchForm):
    loc = forms.CharField(required=False)

    def search(self):
        sqs = super(ListingSearchForm, self).search()

        if not self.is_valid():
            return self.no_query_found()

        print self.cleaned_data['loc']
        #print sqs
        sqs = sqs.filter(location__contains=self.cleaned_data['loc'])
        #print sqs

        return sqs