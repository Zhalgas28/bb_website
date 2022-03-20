from django.db import models


class Contact(models.Model):
    ''' Модель для рассылки по email '''
    email = models.EmailField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email
