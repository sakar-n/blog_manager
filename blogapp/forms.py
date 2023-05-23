from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Blogmodels


class SignUpform(UserCreationForm):
   
    email = forms.EmailField(max_length=254, required=True, widget=forms.EmailInput(attrs={'placeholder':'abc@email.com', 'class':'form-control'}))
    username = forms.CharField(max_length=254, required=True, widget=forms.TextInput(attrs={'placeholder':'username', 'class':'form-control'}))
    first_name = forms.CharField(max_length=254, required=True, widget=forms.TextInput(attrs={'placeholder':'Firstname', 'class':'form-control'}))
    last_name = forms.CharField(max_length=254, required=True, widget=forms.TextInput(attrs={'placeholder':'Lastname', 'class':'form-control'}))
    password1 = forms.CharField(max_length=254, required=True, widget=forms.TextInput(attrs={'placeholder':'password', 'class':'form-control'}))
    password2 = forms.CharField(max_length=254, required=True, widget=forms.TextInput(attrs={'placeholder':'confirmpassword', 'class':'form-control'}))
    
    class Meta:
        model = User
        fields = [
            "email",
            "username",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]


class Blogform(forms.ModelForm):
      
      

      class Meta:
        model = Blogmodels
        fields = ["blog_title", "blog_description", "image"]
