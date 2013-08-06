# -*- coding: utf-8 -*-
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import Context, Template, RequestContext
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.utils.translation import ugettext_lazy as _
from news.models import News
import datetime

def news(request):
    
    menuvar = menu(request)
    
    if menuvar['getarchive']['month'] == None or menuvar['getarchive']['year'] == None:
        news = News.objects.filter(lang=request.LANGUAGE_CODE).order_by('-pub_date')
    else:
        news = News.objects.filter(pub_date__month=menuvar['getarchive']['month'],pub_date__year=menuvar['getarchive']['year'],
                    lang=request.LANGUAGE_CODE).order_by('-pub_date')
        
    paginator = Paginator(news, 4)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        page_news = paginator.page(page)
    except (InvalidPage):
        raise Http404
        
    return render_to_response('news/news.html', {"page_news":page_news,"page":page,"menu":menuvar}, context_instance=RequestContext(request))

def new(request,slug):
    
    try:
        new = News.objects.get(slug=slug)
    except:
        raise Http404
    
    menuvar = menu(request)
    
    return render_to_response('news/details.html', {"new":new,"menu":menuvar}, context_instance=RequestContext(request))

def menu(request):
    
    getarchive = {"month":None,"year":None,}
    
    if request.method == 'GET' and 'mois' in request.GET:
        try:
            temp = request.GET['mois'].split('-')
            getarchive['month'] = int(temp[0])
            getarchive['year'] = int(temp[1])
        except:
            pass
    
    lastestnews = News.objects.filter(lang=request.LANGUAGE_CODE).order_by('-pub_date')[:6]
    months = News.objects.dates('pub_date', 'month').order_by('-pub_date').distinct()
    
    translate_months = (_(u"Janvier"),_(u"Février"),_(u"Mars"),_(u"Avril"),_(u"Mai"),_(u"Juin"),_(u"Juillet"),
                        _(u"Août"),_(u"Septembre"),_(u"Octobre"),_(u"Novembre"),_(u"Décembre"),)
    
    months_list = []
    for datet in months:
        mois = translate_months[datet.month-1]
        obj = {
            'val':str(datet.month)+"-"+str(datet.year),
            'aff':u"%(mois)s %(y)s" % {"mois":mois,"y":str(datet.year)},
            'sel':True if datet.month == getarchive['month'] and datet.year == getarchive['year'] else False,
        }
        if not obj in months_list:
            months_list.append(obj)
    
    return {'lastnews':lastestnews,"archives_months":months_list,"getarchive":getarchive}
