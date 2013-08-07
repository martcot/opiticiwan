from django import template
from news.models import News
from django.template import Context, Template, RequestContext
from django.template.loader import render_to_string
register = template.Library()

@register.simple_tag
def sel_menu_children(request,children):

    return render_to_string('app/sel-menu-children.html', {'children':children}, context_instance=RequestContext(request))