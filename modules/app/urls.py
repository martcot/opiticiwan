from django.conf.urls.defaults import *

urlpatterns = patterns('app.views',
    url(r'^$', 'home', name="home"),
    url(r'^infolettre/desinscription/(?P<guid>.+)/$', 'unsubscription', name="unsubscription"),
    url(r'^contact/$', 'contact', name="contact"),
    url(r'^recherche/', include('haystack.urls')),
)