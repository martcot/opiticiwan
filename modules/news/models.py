# -*- coding: utf-8 -*-
from django.db import models
from django.utils.timezone import localtime
from django.utils.translation import ugettext_lazy as _
from autoslug import AutoSlugField
from django.conf import settings
from tinymce.models import HTMLField
import datetime

class News(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Titre de la nouvelle"))
    lang = models.CharField(max_length=3,choices=settings.LANGUAGES,default='fr', verbose_name=_("Langue"))
    slug = AutoSlugField(populate_from='title', unique=True)
    short_content = models.TextField(verbose_name=_("Court contenu de la nouvelle"))
    content = HTMLField(verbose_name=_("Contenu de la nouvelle"))
    pub_date = models.DateTimeField(verbose_name=_("Date de publication"),default=datetime.datetime.now)
    
    class Meta:
        verbose_name = _("Nouvelle")
        verbose_name_plural = _("Nouvelles")