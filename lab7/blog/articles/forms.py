from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EmployeeRegistrationForm(UserCreationForm):
    email = forms.EmailField(label="Электронная почта", required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")