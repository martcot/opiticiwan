# -*- coding: utf-8 -*-
from django.db import models
from uuidfield import UUIDField
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
import datetime

class Subscription(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Nom"))
    courriel = models.CharField(max_length = 250, verbose_name=_("Courriel"), unique=True)
    sub_date = models.DateTimeField(verbose_name=_("Date de l'inscription"),default=datetime.datetime.now)
    guid = UUIDField(auto=True)
    
    def __str__(self):
        return "%s" % (self.name)
    def __unicode__(self):
        return u'%s' % (self.name)
    
    class Meta:
        verbose_name = _("Inscription")
        verbose_name_plural = _("Inscriptions")