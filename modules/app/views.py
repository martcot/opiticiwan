#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, Template, RequestContext
from django.shortcuts import render_to_response

def home(request):  
        
    return render_to_response('index.html', {}, context_instance=RequestContext(request))
