from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from app.models import Movie
from contact.models import Contact


def send(user_email):
    send_mail(
        'Вы подписалиcь на рассылку',
        'Вам будут приходить уведомления о новых фильмах добавленных на наш сайт BlockBuster.',
        'blackhorse11zhalgas@gmail.com',
        [user_email],
        fail_silently=False,
    )


@receiver(post_save, sender=Movie)
def send_movie(instance, **kwargs):
    name = instance.name
    genre = instance.genre
    year = instance.year
    description = instance.description

    for user_email in Contact.objects.all():
        send_mail(
            f'Обновление на сайте: {name} ({year})',
            f'{description}',
            'blackhorse11zhalgas@gmail.com',
            [user_email],
            fail_silently=False,
        )

