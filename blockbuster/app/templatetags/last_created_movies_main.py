from django import template

from app.models import Movie
from app.service import calc_avg_rating

register = template.Library()

@register.inclusion_tag('app/last_created_movies_main_tpl.html')
def get_last_created_movies_main():
    return {'last_created_movies': Movie.objects.order_by('-created_at')}