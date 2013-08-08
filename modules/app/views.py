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
from app.models import Subscription
from news.models import News
from polls.views import lastpoll
from app.forms import ContactForm,EmailForm

def home(request):  
    
    news = News.objects.filter(lang=request.LANGUAGE_CODE).order_by('-pub_date')[:4]
    poll = lastpoll(request)
    
    if request.POST:
        emailform = EmailForm(request.POST)
        if emailform.is_valid():
            sub = Subscription()
            try:
                sub.name = request.POST['nom']
                sub.courriel = request.POST['courriel']
                sub.save()
                emailform = EmailForm()
                emailform.message = _(u"Merci, votre inscription a été enregistrée.")
                emailform.mtype = "success"
            except Exception as e:
                emailform.message = _(u"Une érreur est survenue.") # + " : " + str(e)
                emailform.mtype = "error"

        else:
            emailform.message = _(u"Tous les champs sont obligatoires.")
            emailform.mtype = "error"
    else:
        emailform = EmailForm()
        
    emailfmsg = request.GET.get('emailfmsg', None)
    emailfmsg_mtype = request.GET.get('mtype', None)

    if not emailfmsg == None and not emailfmsg_mtype == None:
        emailform.message = emailfmsg
        emailform.mtype = emailfmsg_mtype

    return render_to_response('index.html', {"news":news,"poll":poll,"emailform":emailform}, context_instance=RequestContext(request))

def unsubscription(request, guid):
    
    news = News.objects.filter(lang=request.LANGUAGE_CODE).order_by('-pub_date')[:4]
    poll = lastpoll(request)
    
    emailform = EmailForm()
    
    try:
        sub = Subscription.objects.get(guid=guid)
        sub.delete()
        mtype = "success"
        message = _(u"Votre courriel a été retiré de la liste d'envoit.")
        
    except:
        mtype = "error"
        message = _(u"Une érreur est survenue.")
    
    link = urlquote('/',{'emailfmsg':message,'mtype':mtype})
    return HttpResponseRedirect("%(link)s#emailSubscription_open" % {'link':link,})

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

from django.utils.http import urlquote  as django_urlquote
from django.utils.http import urlencode as django_urlencode
from django.utils.datastructures import MultiValueDict

def urlquote(link=None, get={}):
    u'''
    This method does both: urlquote() and urlencode()

    urlqoute(): Quote special characters in 'link'

    urlencode(): Map dictionary to query string key=value&...

    HTML escaping is not done.

    Example:

      urlquote('/wiki/Python_(programming_language)')     --> '/wiki/Python_%28programming_language%29'
      urlquote('/mypath/', {'key': 'value'})              --> '/mypath/?key=value'
      urlquote('/mypath/', {'key': ['value1', 'value2']}) --> '/mypath/?key=value1&key=value2'
      urlquote({'key': ['value1', 'value2']})             --> 'key=value1&key=value2'
    '''
    assert link or get
    if isinstance(link, dict):
        # urlqoute({'key': 'value', 'key2': 'value2'}) --> key=value&key2=value2
        assert not get, get
        get=link
        link=''
    assert isinstance(get, dict), 'wrong type "%s", dict required' % type(get)
    assert not (link.startswith('http://') or link.startswith('https://')), \
        'This method should only quote the url path. It should not start with http(s)://  (%s)' % (
        link)
    if get:
        # http://code.djangoproject.com/ticket/9089
        if isinstance(get, MultiValueDict):
            get=get.lists()
        if link:
            link='%s?' % django_urlquote(link)
        return u'%s%s' % (link, django_urlencode(get, doseq=True))
    else:
        return django_urlquote(link)
