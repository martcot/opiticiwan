# -*- coding: utf-8 -*-
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import Context, Template, RequestContext
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.utils.translation import ugettext_lazy as _
from events.models import Event
import datetime

def events(request):
    events = Event.objects.filter(type="t&l").order_by('-date')
        
    paginator = Paginator(events, 4)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        page_events = paginator.page(page)
    except (InvalidPage):
        raise Http404
        
    return render_to_response('events/events.html', {"page_events":page_events,"page":page}, context_instance=RequestContext(request))

def event(request,slug):
    
    try:
        event = Event.objects.get(slug=slug)
    except:
        raise Http404
    
    return render_to_response('events/details.html', {"event":event,"title":event.title}, context_instance=RequestContext(request))