from django import template
register = template.Library()

@register.filter
def imgurl(value):
    return value.replace('members/static/', '')
