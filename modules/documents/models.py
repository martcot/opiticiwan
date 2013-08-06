# -*- coding: utf-8 -*-
from django.db import models
from django.utils.timezone import localtime
from django.utils.translation import ugettext_lazy as _
from autoslug import AutoSlugField
from django.conf import settings
from documents.extra import ContentTypeRestrictedFileField
import datetime

class Document(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Titre du document"))
    lang = models.CharField(max_length=3,choices=settings.LANGUAGES,default='fr', verbose_name=_("Langue"))
    slug = AutoSlugField(populate_from='title', unique=True)
    short_content = models.TextField(verbose_name=_("Courte description"),blank=True)
    document = ContentTypeRestrictedFileField(
        upload_to='documents',
        content_types=[
               'application/pdf', 
               #'application/msword', 
               #'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        ],
        max_upload_size=104857600
        ,verbose_name=_("Fichier du document (PDF)")
    )
    pub_date = models.DateTimeField(verbose_name=_("Date de publication"),default=datetime.datetime.now)
    category = models.ManyToManyField('Category')
    
    def __str__(self):
        return "%s" % (self.title)
    def __unicode__(self):
        return u'%s' % (self.title)
    
    class Meta:
        verbose_name = _("Document")
        verbose_name_plural = _("Documents")
        
class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name=_(u"Catégorie"))
    lang = models.CharField(max_length=3,choices=settings.LANGUAGES,default='fr', verbose_name=_("Langue"))
    slug = AutoSlugField(populate_from='title', unique=True)
    parent = models.ForeignKey('Category',blank=True, verbose_name=_(u"Catégorie parente"))
    
    @property
    def children(self):
        try:
            children = Category.objects.filter(parent=self)
        except:
            children = None
            
        return children
    
    @property
    def docs(self):
        docs_list = []
        try:
            docs = Document.objects.filter(category=self).order_by('-pub_date')
            for doc in docs:
                if not doc in docs_list:
                    docs_list.append(doc)
                    
            children = self.children
            if children:
                for child in children:
                    child_docs = child.docs
                    if child_docs:
                        docs_list = docs_list + child_docs
        except:
            pass
        
        return docs_list
    
    def __str__(self):
        return "%s" % (self.title)
    def __unicode__(self):
        return u'%s' % (self.title)
    
    class Meta:
        verbose_name = _(u"Catégorie")
        verbose_name_plural = _(u"Catégories")
