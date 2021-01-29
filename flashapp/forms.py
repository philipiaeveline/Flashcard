from django import forms
from .models import Author,Picture,Category,Location,Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class NewPostForm(forms.ModelForm):
    class Meta:
        model = Picture
        exclude = ['likes','user']


class SignUpForm(UserCreationForm):
    email = forms.EmailField(help_text='Enter Email!')
    class Meta:
        model = User
        fields = ('username','email','password1','password2')



class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_pic','bio','username')
