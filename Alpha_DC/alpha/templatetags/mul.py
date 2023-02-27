from django import template

register = template.Library()

@register.filter('multiply')
def multiply(value, arg):
    return float(value) * float(arg)

@register.filter('addition')
def addition(value, arg):
    return float(value) + float(arg)