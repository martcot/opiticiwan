#-*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from galeries.models import Gallery, Photo

def index(request):
    galeries = Gallery.objects.all()
    photos = Photo.objects.all()

    paginator = Paginator(photos, 12)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        page_photos = paginator.page(page)
    except (EmptyPage, InvalidPage):
        page_photos = paginator.page(paginator.num_pages)

    return render_to_response('gallerie/index.html', {"photos":photos, "galeries":galeries,"page_photos":page_photos}, context_instance=RequestContext(request))

def galerie(request, slug):
    galeries = Gallery.objects.all()
    photos = Gallery.objects.get(slug=slug).photos

    paginator = Paginator(photos, 12)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        page_photos = paginator.page(page)
    except (EmptyPage, InvalidPage):
        page_photos = paginator.page(paginator.num_pages)
        
    return render_to_response('gallerie/index.html', {"photos":photos, "galeries":galeries,"page_photos":page_photos}, context_instance=RequestContext(request))
	
