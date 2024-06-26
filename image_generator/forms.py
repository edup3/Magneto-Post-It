from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput

class CreateUserForm(UserCreationForm):

    profile_picture = forms.ImageField(required=False, label='Company logo')
    colors = forms.CharField(label='Company Colors (hex format, separated by comma)', max_length=100)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'profile_picture', 'colors']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
