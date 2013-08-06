from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class GalleryApp(CMSApp):
    name = _("Galeries photos") # give your app a name, this is required
    urls = ["galeries.urls"] # link your app to url configuration(s)

apphook_pool.register(GalleryApp) # register your app