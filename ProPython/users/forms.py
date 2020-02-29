from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile



class UserRgisteForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:

        model = User

        fields = ["username", "email", "password1", "password2"]


class u_form(forms.ModelForm):
    email = forms.EmailField()
    class Meta:

        model = User

        fields = ["username", "email"]

class p_form(forms.ModelForm):
    
    class Meta:

        model = Profile

        fields = ["image"]