# -*- coding: utf-8 -*-
from django.db import models
from autoslug import AutoSlugField
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
import datetime

class PhotoTitle(models.Model):
    photo = models.ForeignKey('Photo')
    title = models.CharField(max_length = 255, verbose_name=_("Titre"))
    lang = models.CharField(max_length=3,choices=settings.LANGUAGES,default='fr', verbose_name=_("Langue"))
    
    class Meta:
        verbose_name = _("Traduction")
        verbose_name_plural = _("Traductions")

class Photo(models.Model):
    photo = models.ImageField(upload_to = "photos", verbose_name=_("Photo"))
    album = models.ManyToManyField("Gallery")
    pub_date = models.DateTimeField(verbose_name=_("Date de publication"),default=datetime.datetime.now)
    
    def __str__(self):
        try:
            PTitle = PhotoTitle.objects.filter(photo=self)[0]
            title = PTitle.title
        except:
            title = _("Sans titres")

        return "%s" % (title)
    
    def __unicode__(self):
        try:
            PTitle = PhotoTitle.objects.filter(photo=self)[0]
            title = PTitle.title
        except:
            title = _("Sans titres")
        
        return u'%s' % (title)
    
    class Meta:
        verbose_name = _("Photo")
        verbose_name_plural = _("Photos")

class Gallery(models.Model):
    title = models.CharField(max_length = 255, verbose_name=_("Titre"))
    slug = AutoSlugField(populate_from='title', unique=True)
    lang = models.CharField(max_length=3,choices=settings.LANGUAGES,default='fr', verbose_name=_("Langue"))
    pub_date = models.DateTimeField(verbose_name=_("Date de publication"),default=datetime.datetime.now)

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