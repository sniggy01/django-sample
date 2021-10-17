from django import template

register = template.Library()

# ---Registering the filter using decorators---
@register.filter(name='cut')
def cut_temp(value,arg):
    """
    This cuts out all values of "arg" from the string.
    """

    return value.replace(arg,'')

# ---Another way to register the filter---
# register.filter('cut',cut_temp)
