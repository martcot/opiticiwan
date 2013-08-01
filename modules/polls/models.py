# -*- coding: utf-8 -*-
from django.db import models
from django.utils.timezone import localtime
from django.utils.translation import ugettext_lazy as _
from autoslug import AutoSlugField
from django.conf import settings
from uuidfield import UUIDField
import datetime

class Poll(models.Model):
    question = models.CharField(max_length=255, verbose_name=_("Question du sondage"))
    slug = AutoSlugField(populate_from='question', unique=True)
    lang = models.CharField(max_length=3,choices=settings.LANGUAGES,default='fr', verbose_name=_("Langue"))
    pub_date = models.DateTimeField(verbose_name=_("Date de publication"),default=datetime.datetime.now)
    
    @property 
    def choices(self):
        return PollChoices.objects.filter(poll=self)
    
    def hasvoted(self,sessionid):
        voted = False
        for choice in self.choices:
            if choice.answers.filter(sessionid=sessionid).count() > 0:
                voted = True
                break
            
        return voted
    
    class Meta:
        verbose_name = _("Sondage")
        verbose_name_plural = _("Sondages")
    
class PollAnswers(models.Model):
    pollchoice = models.ForeignKey('PollChoices')
    sessionid = UUIDField(auto=True)
    datetime = models.DateTimeField(default=datetime.datetime.now)
    
class PollChoices(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=255, verbose_name=_(u"Réponse possible"))
    
    @property 
    def answers(self):
        return PollAnswers.objects.filter(pollchoice=self)
    
    class Meta:
        verbose_name = _(u"Réponse")
        verbose_name_plural = _(u"Réponses")