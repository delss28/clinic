from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from main.models import Service
from users.models import Appointment, User


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
    patronymic = forms.CharField(required=False)
    username = forms.CharField()
    email = forms.CharField()
    number = forms.CharField()
    dateOfBirth = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()


class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "avatar",
            "first_name",
            "last_name",
            "patronymic",
            "username",
            "email",
            "number",
        )

    avatar = forms.ImageField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    patronymic = forms.CharField(required=False)
    username = forms.CharField()
    email = forms.CharField()
    number = forms.CharField()


class UserAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = (
            "id_user",
            "id_service",
            "appointment_date",
            "appointment_time",
        )
    id_user = forms.ModelChoiceField(queryset=User.objects.all())
    id_service = forms.ModelChoiceField(queryset=Service.objects.all())
    appointment_date = forms.DateField()
    appointment_time = forms.TimeField()