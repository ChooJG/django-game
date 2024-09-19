from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    last_name = forms.CharField(label="닉네임", required=True)

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "last_name")

