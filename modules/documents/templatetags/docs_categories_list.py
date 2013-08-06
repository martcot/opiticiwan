from django import template
from news.models import News
from django.template import Context, Template, RequestContext
from django.template.loader import render_to_string
register = template.Library()

@register.simple_tag
def docs_categories_list(request,cats):

    return render_to_string('documents/cats_list.html', {'cats':cats}, context_instance=RequestContext(request))