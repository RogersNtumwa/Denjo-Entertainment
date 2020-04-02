from .models import movie
from django.forms import ModelForm, Textarea
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from accounts.models import profile


class moviesForm(ModelForm):
    class Meta:
        model = movie
        fields = ('title', 'genre', 'description', 'logo', 'moviefile')


class registerform(UserCreationForm):
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserupdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileupdateForm(ModelForm):
    class Meta:
        model = profile
        fields = ['image', ]
