# -*- coding: utf-8 -*-
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import Context, Template, RequestContext
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from documents.models import *
import datetime

def index(request):
    
    menuvar = menu(request)

    docs = Document.objects.all().order_by('-pub_date')
    paginator = Paginator(docs, 6)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        page_docs = paginator.page(page)
    except (InvalidPage):
        raise Http404
        
    return render_to_response('documents/index.html', {"page_docs":page_docs,"page":page,"menu":menuvar}, context_instance=RequestContext(request))

def cat(request,slug):
    
    try:
        category = Category.objects.get(slug=slug)
    except:
        raise Http404
    
    menuvar = menu(request)

    docs = category.docs
    paginator = Paginator(docs, 6)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        page_docs = paginator.page(page)
    except (InvalidPage):
        raise Http404
        
    return render_to_response('documents/index.html', {"category":category, "page_docs":page_docs,"page":page,"menu":menuvar,"title":category.title}, context_instance=RequestContext(request))

def menu(request):
    
    firstcats = Category.objects.filter(parent=None,lang=request.LANGUAGE_CODE).order_by('title')
    
    return {"firstcats":firstcats}

def doc(request,slug):
    
    try:
        doc = Document.objects.get(slug=slug)
    except:
        raise Http404
    
    with open(settings.MEDIA_ROOT + "/" + str(doc.document), 'r') as pdf:
        response = HttpResponse(pdf.read(), mimetype='application/pdf')
        response['Content-Disposition'] = 'inline;filename='+doc.slug+'.pdf'
        return response
    pdf.closed
