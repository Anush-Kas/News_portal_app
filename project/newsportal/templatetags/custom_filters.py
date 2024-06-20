from django import template


register = template.Library()


@register.filter()
def big_title(title):
   return title.upper()

