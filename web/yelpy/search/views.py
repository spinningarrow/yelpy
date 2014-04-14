from django.shortcuts import render
from  django.http import HttpResponse
from search_forms import ListingSearchForm
import pysolr
# Create your views here.

def home(request):
    return HttpResponse("HOME PAGE")

def searchview(request):
    return render(request, 'searchview.html')

def searchthings(request):
    form = ListingSearchForm(request.GET)
    results = form.search()

    return render(request, 'searchresults.html', {'results':results})
