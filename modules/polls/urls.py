from django.conf.urls.defaults import *

urlpatterns = patterns('polls.views',
    url(r'^sondages/(?P<slug>.+)/(?P<id>.+)/$', 'vote', name="vote"),
)