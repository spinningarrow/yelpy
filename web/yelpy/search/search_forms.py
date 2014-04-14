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
		#you can list your filters here. Below is a filter on the location attribute
        sqs = sqs.filter(location__contains=self.cleaned_data['loc'])
        #print sqs
		
		#this returns 1 instance of search query.
        return sqs