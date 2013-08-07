from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView
from news.feeds import LatestEntriesFeed

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('app.urls')),
    url(r'^', include('polls.urls')),
    url(r'^rss/$', LatestEntriesFeed(), name="rss_feed"),
    
    (r'^admin/', include(admin.site.urls)),
    (r'^tinymce/', include('tinymce.urls')),
    (r'^grappelli/', include('grappelli.urls')),
	(r'^comments/', include('django.contrib.comments.urls')),
	url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/filebrowser/', include('filebrowser.urls')),
	url(r'^robot.txt', TemplateView.as_view(template_name="robot.txt")),
    url(r'^', include('cms.urls')),
)

if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns
