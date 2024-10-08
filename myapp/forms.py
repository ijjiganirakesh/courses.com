from django import forms
from .models import *
from django .contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class courseform(forms.ModelForm):
    class Meta:
        model=course
        fields='__all__'

class registerform(forms.ModelForm):
    class Meta:
        model=Account
        fields=['username','password','email','phone','address']

    def save(self):
        user = super().save(commit=False)
        user.password=make_password(self.cleaned_data['password'])
        user.save()
        return user
    
class loginform(forms.Form):
    username=forms.CharField(max_length=25)
    password=forms.CharField(max_length=25,widget=forms.PasswordInput)

