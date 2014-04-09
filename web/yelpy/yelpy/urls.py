from django.conf.urls import patterns, include, url

from django.contrib import admin
from search import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yelpy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', views.home),
    url(r'^search/', include('haystack.urls')),


)
