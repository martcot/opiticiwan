from django.conf.urls.defaults import *

urlpatterns = patterns('events.views',
    url(r'^$', 'events', name="events"),
    url(r'^(?P<slug>.+)/$', 'event', name="event"),
)