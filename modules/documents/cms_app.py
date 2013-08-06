from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class DocumentsApp(CMSApp):
    name = _("Documents") # give your app a name, this is required
    urls = ["documents.urls"] # link your app to url configuration(s)

apphook_pool.register(DocumentsApp) # register your app