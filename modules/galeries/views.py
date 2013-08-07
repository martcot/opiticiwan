#-*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from galeries.models import Gallery, Photo

def index(request):
    galeries = Gallery.objects.filter(lang=request.LANGUAGE_CODE).order_by('-pub_date')
    photos = Photo.objects.all()

    paginator = Paginator(photos, 12)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        page_photos = paginator.page(page)
    except (InvalidPage):
        raise Http404

    return render_to_response('galeries/index.html', {"photos":photos, "galeries":galeries,"page_photos":page_photos,"page":page}, context_instance=RequestContext(request))

def galerie(request, slug):
    galeries = Gallery.objects.filter(lang=request.LANGUAGE_CODE).order_by('-pub_date')
    
    try:
        galerie = Gallery.objects.get(slug=slug)
    except:
        raise Http404
    
    photos = galerie.photos

    paginator = Paginator(photos, 12)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        page_photos = paginator.page(page)
    except (InvalidPage):
        raise Http404
        
    return render_to_response('galeries/index.html', {"photos":photos, "galeries":galeries, "galerie":galerie, "page_photos":page_photos,"page":page,"title":galerie.title}, context_instance=RequestContext(request))
	
