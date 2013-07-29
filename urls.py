from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
	(r'^ckeditor/', include('ckeditor.urls')),
	(r'^comments/', include('django.contrib.comments.urls')),
	url(r'^admin_tools/', include('admin_tools.urls')),
	url(r'^robot.txt', TemplateView.as_view(template_name="robot.txt")),
	url(r'^', include('app.urls')),
    url(r'^', include('cms.urls')),
)

if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns
