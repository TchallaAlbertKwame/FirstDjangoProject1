from django import forms
from .models import RegistrationData


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=150,
                               widget=forms.TextInput(attrs={
                                   "class": "form-control",
                                   "placeholder": "Username"

                               }))
    password = forms.CharField(max_length=150,
                               widget=forms.PasswordInput(attrs={
                                   "class": "form-control",
                                   "placeholder": "password"

                               }))
    Email = forms.CharField(max_length=150,
                            widget=forms.EmailInput(attrs={
                                "class": "form-control",
                                "placeholder": "Email"

                            }))
    Phone = forms.CharField(max_length=150,
                            widget=forms.NumberInput(attrs={
                                "class": "form-control",
                                "placeholder": "Phone"

                            }))


class RegistrationModal(forms.ModelForm):
    class Meta:
        model = RegistrationData

        fields = ['username',
                  'password',
                  'Email',
                  'Phone']
