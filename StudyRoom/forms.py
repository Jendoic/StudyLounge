from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, CustomUser
from django.contrib.auth.models import User


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = "__all__"
        exclude = ['host', 'participants']


class UserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username','email', 'name', 'bio']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder':'Username'}),
              'email': forms.TextInput(attrs={'placeholder':'Abc@gmail.com'}),
              'name': forms.TextInput(attrs={'placeholder':'Your name'}),
              'bio': forms.Textarea(attrs={'placeholder':'Tell us about yourself', 'id': 'wordCount'}),
             
        }
        
class CustomUserForm(UserCreationForm):
    password1 = forms.CharField(label='Password',  widget=forms.PasswordInput(attrs={'id':'password1' ,'placeholder':'Password', }))
    password2 = forms.CharField(label='Enter Password Again',  widget=forms.PasswordInput(attrs={ 'id': 'password2','placeholder':'Confirm Password'}))

    class Meta:
        model = CustomUser
        fields = ('username','email', 'password1', 'password2',)
        
        widgets = {
            'username': forms.TextInput(attrs={'placeholder':'Username'}),
              'email': forms.TextInput(attrs={'placeholder':'Abc@gmail.com'}),
             
        }