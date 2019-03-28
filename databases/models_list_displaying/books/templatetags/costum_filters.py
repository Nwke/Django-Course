from django import template

register = template.Library()


@register.filter
def convert_date(value):
    return value.strftime("%Y-%m-%d")
