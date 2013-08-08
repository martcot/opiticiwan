from django import template
from django.template import Context, Template, RequestContext
from django.template.loader import render_to_string
register = template.Library()

@register.simple_tag
def menu_children(request,children):

    return render_to_string('app/menu_children.html', {'children':children}, context_instance=RequestContext(request))