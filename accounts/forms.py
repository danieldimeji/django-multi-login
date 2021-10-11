from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate


# Using django's custom user models and form creation

class SignUpForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'autofocus': False})
        self.fields['first_name'].widget.attrs.update({'autofocus': True})

    first_name = forms.CharField(
        required = True,
        widget = forms.TextInput(
            attrs = {
                'class' : 'input100',
                'name' : 'first-name',
                'type' : 'text',
                'placeholder': 'Firstname'
            }
        )
    )
    
    last_name = forms.CharField(
        required = True,
        widget = forms.TextInput(
            attrs = {
                'class' : 'input100',
                'name' : 'last-name',
                'type' : 'text',
                'placeholder': 'Lastname'
            }
        )
    )
    
    email = forms.EmailField(
        required = True,
        widget = forms.EmailInput(
            attrs = {
                'class' : 'input100',
                'name' : 'email',
                'type' : 'email',
                'placeholder': 'Email'
            }
        )
    )

    username = forms.CharField(
        required = True,
        widget = forms.TextInput(
            attrs = {
                'class' : 'input100',
                'name' : 'username',
                'type' : 'text',
                'placeholder': 'Username'
            }
        )
    )
    
    password1 = forms.CharField(
        required = True,
        widget = forms.PasswordInput(
            attrs = {
                'class' : 'input100',
                'name' : 'password',
                'type' : 'password',
                'placeholder': 'Password'
            }
        )
    )
    
    password2 = forms.CharField(
        required = True,
        widget = forms.PasswordInput(
            attrs = {
                'class' : 'input100',
                'name' : 'confirm-password',
                'type' : 'password',
                'placeholder': 'Confirm Password'
            }
        )
    )

    class Meta:
        model = User
        fields = ['email', 'username','first_name','last_name', 'password1', 'password2']

    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs_username = User.objects.filter(username=username)
        qs_email = User.objects.filter(email=username)

        if qs_username.exists() or qs_email.exists():
            raise forms.ValidationError('Username is not available[Username]')
        return username


    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs_email = User.objects.filter(email=email)
        qs_username = User.objects.filter(username=email)

        if qs_username.exists() or qs_email.exists():
            raise forms.ValidationError('Username is not available [Email]')
        return email


class SignInForm(forms.Form):
    
    username_email = forms.CharField(
        required = True,
        widget = forms.TextInput(
            attrs = {
                'class' : 'input100',
                'name' : 'username',
                'type' : 'text',
                'placeholder': 'Username'
            }
        )
    )

    password = forms.CharField(
        required = True,
        widget = forms.PasswordInput(
            attrs = {
                'class' : 'input100',
                'name' : 'password',
                'type' : 'password',
                'placeholder': 'Password'
            }
        )
    )