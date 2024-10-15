from django import template
from urllib.parse import urlparse

register = template.Library()

@register.filter
def url_hostname(value):
    return urlparse(value).hostname
