#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf import settings
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, Template, RequestContext
from django.shortcuts import render_to_response
from django.utils.translation import ugettext_lazy as _
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from news.models import News
from polls.views import lastpoll
from app.forms import ContactForm

def home(request):  
    
    news = News.objects.filter(lang=request.LANGUAGE_CODE).order_by('-pub_date')[:4]
    poll = lastpoll(request)

    return render_to_response('index.html', {"news":news,"poll":poll}, context_instance=RequestContext(request))

def contact(request):  
    
    if request.POST:
        contactform = ContactForm(request.POST)
        if contactform.is_valid():
            message = render_to_string('app/email.html', {'form': contactform,})
            msg = EmailMultiAlternatives('Contact de opiticiwan.ca : '+request.POST['sujet'].encode('utf8'), message, request.POST['courriel'], [settings.SEND_EMAILS_TO])
            msg.attach_alternative(message, "text/html")
            msg.send()
            contactform = ContactForm()
            contactform.message = _(u"Votre message a bien été envoyé, nous vous contacterons sous peu.")
            contactform.mtype = "success"
        else:
            contactform.message = _(u"Tous les champs sont obligatoires.")
            contactform.mtype = "error"
    else:
        contactform = ContactForm()

    return render_to_response('contact.html', {"form":contactform}, context_instance=RequestContext(request))
