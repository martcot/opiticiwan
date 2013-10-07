# -*- coding: utf-8 -*-
from django.db import models
from django.utils.timezone import localtime
from cms.models import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from autoslug import AutoSlugField
from django.conf import settings
from tinymce.models import HTMLField
import datetime

def EventType():
    return (
        ('sdc', _(u'Séance du conseil')),
        ('t&l', _(u'Tourisme et loisirs')),
    )

class Event(models.Model):
    title = models.CharField(max_length=255, verbose_name=_(u"Titre de l'évènement"))
    type = models.CharField(max_length=4,
                              choices=EventType(),
                              default='t&l',
                              verbose_name = _("Type d'évènement"),)
    slug = AutoSlugField(populate_from='title', unique=True)
    short_content = models.TextField(verbose_name=_("Courte description"))
    content = HTMLField(verbose_name=_("Description"))
    date = models.DateTimeField(verbose_name=_(u"Date de l'évènement"),default=datetime.datetime.now)
    
    def __str__(self):
        return "%s" % (self.title)
    def __unicode__(self):
        return u'%s' % (self.title)
    
    class Meta:
        verbose_name = _(u"Évènement")
        verbose_name_plural = _(u"Évènements")