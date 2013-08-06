from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('',
	(r'^$', 'galeries.views.index'),
    (r'^(?P<slug>.+)/$', 'galeries.views.galerie'),
)

