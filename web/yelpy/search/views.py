from django.shortcuts import render
from django.http import HttpResponse
from django.forms.models import model_to_dict
from yelpy.models import All
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
    query = ''

    results = {
        'food': SearchQuerySet().models(shopslistings), # shops is food (wtf, why?!)
        'shops': SearchQuerySet().models(foodslistings),
        'sports': SearchQuerySet().models(sportslistings),
        'arts': SearchQuerySet().models(artslistings),
    }

    # Get current user's preferences
    userId = request.session.get('fb_user_id', '')
    if (userId):

        # Do some lookup magic and store the result in the appropriate category
        user_prefs = model_to_dict(All.objects.get(id=userId))
        prefs_list = [pref for pref in user_prefs if user_prefs[pref] == True]

        prefs_category_map = All.category_dict()

        for item in prefs_list:
            category = prefs_category_map[item]
            results[category] = results[category].filter_or(content=item)

    if request.method == 'POST':
        query = request.POST.get('query_filter', '')
        for key in results:
            results[key] = results[key].filter(content=query)

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
    # foodResults = SearchQuerySet().auto_query('ice cream').boost('chocolate', 1.1)
    # artsResults = SearchQuerySet().filter(content='dance')
    # sportsResults = SearchQuerySet().filter(content='soccer')
    # shoppingResults = SearchQuerySet().filter(content='ion')
    return render(request, 'automaticquerying.html', { 'results': results, 'query_filter': query, 'fb_id': request.session.get('fb_user_id', '') })
