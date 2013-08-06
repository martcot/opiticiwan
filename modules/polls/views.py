#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import Context, Template, RequestContext
from django.template.loader import render_to_string
from django.shortcuts import render_to_response
from polls.models import *

def lastpoll(request):  
    
    try:
        poll = Poll.objects.filter(lang=request.LANGUAGE_CODE).order_by('-pub_date')[0]

        session = request.session.get('voted_'+poll.slug, False)

        if session:
            hasvoted = poll.hasvoted(session)
        else:
            hasvoted = False
        
    except:
        poll = None
        hasvoted = False
    
    if hasvoted:
        return render_to_string('polls/poll_voted.html', {'poll':poll}, context_instance=RequestContext(request))
    else:
        return render_to_string('polls/poll.html', {'poll':poll}, context_instance=RequestContext(request))

def vote(request,slug,id):
    
    try:
        poll = Poll.objects.get(slug=slug)
    except:
        raise Http404
    
    session = request.session.get('voted_'+slug, False)
    if session:
        hasvoted = poll.hasvoted(session)
    else:
        hasvoted = False
        
    if not hasvoted:
        print "create"
        answer = PollAnswers.objects.create(pollchoice=PollChoices.objects.get(id=id,poll=poll))
        request.session['voted_'+slug] = answer.sessionid
    
    return HttpResponseRedirect("/#sondage")