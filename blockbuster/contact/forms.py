from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    ''' Форма для рассылки по email '''
    class Meta:
        model = Contact
        fields = ('email',)




