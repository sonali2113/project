from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'email': forms.EmailInput(attrs={
                'required': True,
                'placeholder': 'lisa@example.com',
                'autofocus': True
            }),
            'username': forms.TextInput(attrs={
                'placeholder': 'lisamora',
            })
        }

    def _init_(self, *args, **kwargs):
        super(RegisterUserForm, self)._init_(*args, **kwargs)
        self.fields['password1'].widget.attrs = {'placeholder': 'password'}
        self.fields['password2'].widget.attrs = {'placeholder': 'confirm password'}

class LoginForm(AuthenticationForm):
    class Meta:
        fields = '_all_'