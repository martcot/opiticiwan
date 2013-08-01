#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, Template, RequestContext
from django.shortcuts import render_to_response
from news.models import News
from polls.views import lastpoll

def home(request):  
    
    news = News.objects.filter(lang=request.LANGUAGE_CODE).order_by('-pub_date')[:4]
    poll = lastpoll(request)

    return render_to_response('index.html', {"news":news,"poll":poll}, context_instance=RequestContext(request))
