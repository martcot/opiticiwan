from django.conf.urls.defaults import *

urlpatterns = patterns('news.views',
    url(r'^nouvelles/$', 'news', name="news"),
    url(r'^nouvelles/(?P<slug>.+)/$', 'new', name="new"),
)