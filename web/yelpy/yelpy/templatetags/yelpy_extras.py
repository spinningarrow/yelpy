from django import template
from django.template.defaultfilters import stringfilter
import json

register = template.Library()

@register.filter
@stringfilter
def address(value):
    json_obj = json.loads(value)
    return ', '.join(json_obj['display_address'])
