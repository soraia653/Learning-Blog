from django import template

register = template.Library()

@register.filter
def get_count(dictionary, key):
    return dictionary[key]['count']

@register.filter
def get_tags(dictionary, key):
    return dictionary[key]['tags']