from django import forms
from login.models import User


class PersonForm(forms.ModelForm):
    firstName = forms.CharField(max_length=30, help_text="Enter Your First Name")
    lastName = forms.CharField(max_length=30, help_text="Enter Your Last Name")
    emailAddress = forms.CharField(max_length=30, help_text="Enter Email Address")
    password = forms.CharField(max_length=30,min_length=6,)

    class Meta:
        model = User
        fields = ('firstName', 'lastName', 'emailAddress', 'password')

