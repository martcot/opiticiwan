# -*- coding: utf-8 -*-
from django.db import models
from autoslug import AutoSlugField
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
import datetime

class Conseiller(models.Model):
    nom = models.CharField(max_length = 255, verbose_name=_("Nom complet"))
    photo = models.ImageField(upload_to = "conseillers", verbose_name=_("Photo"))
    titre = models.CharField(max_length = 255, verbose_name=_("Titre au conseil"))
    
    def __str__(self):
        return "%s" % (self.nom)
    
    def __unicode__(self):
        return u'%s' % (self.nom)
    
    class Meta:
        verbose_name = _("Conseiller")
        verbose_name_plural = _("Conseillers")
        
class Contact(models.Model):
    nom = models.CharField(max_length = 255, verbose_name=_("Nom complet"))
    poste = models.CharField(max_length = 255, verbose_name=_(u"Poste occupé"))
    tel = models.CharField(max_length = 255, verbose_name=_(u"Numéro de téléphone"))
    email = models.EmailField(max_length = 255, verbose_name=_("Courriel"))
    
    def __str__(self):
        return "%s" % (self.nom)
    
    def __unicode__(self):
        return u'%s' % (self.nom)
    
    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")