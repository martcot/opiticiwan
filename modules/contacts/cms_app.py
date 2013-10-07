from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class ContactsApp(CMSApp):
    name = _("Contacts") # give your app a name, this is required
    urls = ["contacts.urls"] # link your app to url configuration(s)

apphook_pool.register(ContactsApp) # register your app