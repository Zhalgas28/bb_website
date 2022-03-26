from django import template

from app.models import Rating

register = template.Library()


@register.simple_tag(name='calc_avg_rating')
def calc_avg_rating(movie_id):
    ratings = Rating.objects.filter(movie=movie_id)
    res = 0
    for rating in ratings:
        res += rating.star.star
    if len(ratings):
        return res / len(ratings)