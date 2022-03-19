from django import template

from app.models import Movie

register = template.Library()

@register.inclusion_tag('app/popular_movies_main_tpl.html')
def get_popular_movies_main():
    return {'popular_movies': Movie.objects.order_by('created_at')}