from django import template

from app.models import Movie

register = template.Library()

@register.inclusion_tag('app/last_movies_tpl.html')
def get_last_movies():
    return {'last_movies': Movie.objects.order_by('-year')}