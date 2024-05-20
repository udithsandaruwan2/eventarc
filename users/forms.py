from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name':'Name', 
        }
        
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control form-control-xl', 'placeholder': 'Name', 'type':'text'},
        )

        self.fields['email'].widget.attrs.update(
            {'class': 'form-control form-control-xl', 'placeholder':'Email', 'type':'text'}
        )

        self.fields['username'].widget.attrs.update(
            {'class': 'form-control form-control-xl', 'placeholder': 'Username', 'type':'text'}
        )

        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control form-control-xl', 'placeholder': 'Password', 'type':'password'}
        )

        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control form-control-xl', 'placeholder': 'Confirm Password', 'type':'password'}
        )


