from django.conf.urls.defaults import *

urlpatterns = patterns('news.views',
    url(r'^$', 'news', name="news"),
    url(r'^(?P<slug>.+)/$', 'new', name="new"),
)