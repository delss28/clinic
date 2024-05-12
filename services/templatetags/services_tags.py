from django import template

from main.models import Service

register = template.Library()

@register.simple_tag()
def tag_services():
    return Service.objects.all()