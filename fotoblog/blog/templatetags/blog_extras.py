from django.template import Library

register = Library()

@register.filter
def model_type(instance):
    return type(instance).__name__