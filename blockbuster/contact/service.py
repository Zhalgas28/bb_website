from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'Вы подписалиcь на рассылку',
        'Вам будут приходить уведомления о новых фильмах добавленных на наш сайт BlockBuster.',
        'blackhorse11zhalgas@gmail.com',
        [user_email],
        fail_silently=False,
    )
