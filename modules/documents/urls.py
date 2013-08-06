from django.conf.urls.defaults import *

urlpatterns = patterns('documents.views',
    url(r'^$', 'index', name="index"),
    url(r'^cat/(?P<slug>.+)/$', 'cat', name="cat"),
)