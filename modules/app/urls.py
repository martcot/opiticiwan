from django.conf.urls.defaults import *

urlpatterns = patterns('app.views',
    url(r'^$', 'home', name="home"),
    url(r'^contact/$', 'contact', name="contact"),
    url(r'^recherche/', include('haystack.urls')),
)