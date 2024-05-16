from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import User


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


    username = forms.CharField()
    password = forms.CharField()
    


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "patronymic",
            "username",
            "email",
            "number",
            "dateOfBirth",
            "password1",
            "password2",
        )


    first_name = forms.CharField()
    last_name = forms.CharField()
    patronymic = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    number = forms.CharField()
    dateOfBirth = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()


    