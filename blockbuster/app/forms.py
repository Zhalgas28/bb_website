from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms

from .models import RatingStar, Rating


class UserRegistrationForm(forms.ModelForm):
    ''' Форма для регистрации пользователей '''
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class UserLoginForm(AuthenticationForm):
    ''' Форма аутентификации пользователя '''
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)


class ReviewsForm(forms.Form):
    ''' Форма отзыва '''
    text = forms.CharField(widget=forms.Textarea)


class RatingForm(forms.ModelForm):
    star = forms.ModelChoiceField(queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None)

    class Meta:
        model = Rating
        fields = ('star',)

