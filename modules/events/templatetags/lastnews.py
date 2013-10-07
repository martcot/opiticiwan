from django import template
from news.models import News
from django.template import Context, Template, RequestContext
from django.template.loader import render_to_string
register = template.Library()
@register.filter(name='lastnews')
def lastnews(request):
    lastnews = News.objects.filter(lang=request.LANGUAGE_CODE).order_by('-pub_date')[:6]
    return render_to_string('news/lastnews.html', {'lastnews':lastnews}, context_instance=RequestContext(request))