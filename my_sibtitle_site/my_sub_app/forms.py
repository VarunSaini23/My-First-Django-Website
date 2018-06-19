from django import forms
from . import models
class Sign_up(forms.ModelForm):
    password=forms.CharField(max_length=32,widget=forms.PasswordInput)
    class Meta():
        model=models.Signup
        fields="__all__"
        
