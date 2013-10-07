#-*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.shortcuts import render_to_response
from contacts.models import Conseiller

def conseil(request):
    conseil = Conseiller.objects.all()

    return render_to_response('contacts/conseil.html', {"conseil":conseil,}, context_instance=RequestContext(request))