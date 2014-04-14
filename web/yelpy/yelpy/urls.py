from django.conf.urls import patterns, include, url

from django.contrib import admin
from search import views

admin.autodiscover()

urlpatterns = patterns('',


	url(r'^$', 'yelpy.views.index', name='home'),
	url(r'^yelpy/profile/', 'yelpy.views.profile', name='profile'),
	url(r'^yelpy/search2/', 'yelpy.views.search2', name='search2'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^search/', include('haystack.urls')),
	url(r'^search/', views.searchview),
    url(r'^searchthings/', views.searchthings),


)
