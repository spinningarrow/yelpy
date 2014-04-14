from django.shortcuts import render
from  django.http import HttpResponse
from search_forms import ListingSearchForm
from models import *
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

from haystack.query import SearchQuerySet

def automaticQuerying(request):
    #results = SearchQuerySet().all()
    #userFoodPreference = some function that gets the stored food preference
    #userArtsPreference = some function that gets the stored arts preference
    #userSportsPreference = some function that gets the stored arts preference
    #userShoppingPreference = some function that gets the stored arts preference
    #foodResults = SearchQuerySet().filter(FILL IN YOUR PREFERENCE FILTERS HERE).models(foodslistings)
    #artsResults = SearchQuerySet().filter(FILL IN YOUR PREFERENCE FILTERS HERE).models(artslistings)
    #sportsResults = SearchQuerySet().filter(FILL IN YOUR PREFERENCE FILTERS HERE).models(sportslistings)
    #shoppingResults = SearchQuerySet().filter(FILL IN YOUR PREFERENCE FILTERS HERE).models(shopslistings)

    #below is an example where i search for the stuff based on some preference. I did not limit search by model. you can, but foodslistings seem to fare poorly if you limit them.
    #you will need to supply your own code to retrieve the user's preferences
    #you can try to store user specific special preferences such as flavor and then use the boost feature to increase it's ranking
    #do be aware that if the preference is not available, the query might backfire! e.g. boosting 'peppermint' returns 0 queries for a query on ice cream
    #boosting is very sensitive! don't overuse.
    #you can do negative boosting to decrease it's score. for example, if the user doesn't like 'strawberry', do a boost of 0.9 to decrease it's relevance.
    #you can retrieve results count by using .count()
    foodResults = SearchQuerySet().auto_query('ice cream').boost('chocolate', 1.1)
    artsResults = SearchQuerySet().filter(content='dance')
    sportsResults = SearchQuerySet().filter(content='soccer')
    shoppingResults = SearchQuerySet().filter(content='ion')
    return render(request, 'automaticquerying.html', {'foodResults':foodResults, 'artsResults':artsResults, 'sportsResults':sportsResults, 'shoppingResults':shoppingResults})
