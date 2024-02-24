from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')

    username = forms.CharField(
        error_messages={
            'required': 'Email or Username is required!',
        }
    )
    password = forms.CharField(
        error_messages={
            'required': 'Password is required!',
        }
    )


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(
        min_length=5,
        max_length=50,
        error_messages={
            'required': 'Username is required!',
            'min_length': 'Username must be at least 5 characters long!',
            'max_length': 'Username must be at most 50 characters long!',
        }
    )
    email = forms.EmailField(
        min_length=5,
        max_length=100,
        error_messages={
            'required': 'Email is required!',
            'min_length': 'Email must be at least 5 characters long!',
            'max_length': 'Email must be at most 100 characters long!',
        }
    )
    password1 = forms.CharField(
        error_messages={
            'required': 'Password is required!',
        }
    )
    password2 = forms.CharField(
        error_messages={
            'required': 'Confirm password is required!',
        }
    )
