from django import template
from galeries.models import *
from django.template import Context, Template, RequestContext
from django.utils.translation import ugettext_lazy as _
register = template.Library()

@register.simple_tag
def phototitle(lang,id):
    try:
        PTitle = PhotoTitle.objects.filter(photo_id=id,lang=lang)[0]
        title = PTitle.title
    except:
        title = _("Sans titres")

    return "%s" % (title)