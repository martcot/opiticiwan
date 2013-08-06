# -*- coding: utf-8 -*-
from django.db import models
from autoslug import AutoSlugField
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class Photo(models.Model):
    photo = models.ImageField(upload_to = "photos", verbose_name=_("Photo"))
    album = models.ManyToManyField("Gallery")
    
    class Meta:
        verbose_name = _("Photo")
        verbose_name_plural = _("Photos")

class Gallery(models.Model):
    title = models.CharField(max_length = 255, verbose_name=_("Titre"))
    slug = AutoSlugField(populate_from='title', unique=True)
    lang = models.CharField(max_length=3,choices=settings.LANGUAGES,default='fr', verbose_name=_("Langue"))

    @property
    def photos(self):
        return Photo.objects.filter(album = self)
    
    def __str__(self):
        return "%s" % (self.title)
    def __unicode__(self):
        return u'%s' % (self.title)
    
    class Meta:
        verbose_name = _("Gallerie")
        verbose_name_plural = _("Galleries")

class PhotoTitle(models.Model):
    photo = models.ForeignKey('Photo')
    title = models.CharField(max_length = 255, verbose_name=_("Titre"))
    lang = models.CharField(max_length=3,choices=settings.LANGUAGES,default='fr', verbose_name=_("Langue"))
    
    class Meta:
        verbose_name = _("Traduction")
        verbose_name_plural = _("Traductions")