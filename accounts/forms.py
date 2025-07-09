from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
import pyotp

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.totp_secret = pyotp.random_base32()
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    token = forms.CharField(label="Authenticator Code")
