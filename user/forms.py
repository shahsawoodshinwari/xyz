"""form layer of the user application"""
from django import forms
from django.contrib.auth.models import User


# Create your forms here
class LoginForm(forms.ModelForm):
    """user login form"""

    class Meta:
        model = User
        fields = ("email", "password")
