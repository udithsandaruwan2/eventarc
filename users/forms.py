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
            {'class': 'form-control form-control-xl', 'placeholder': 'eg : Udith Sandaruwan', 'type':'text'},
        )

        self.fields['email'].widget.attrs.update(
            {'class': 'form-control form-control-xl', 'placeholder':'eg : udith@eventarc.com', 'type':'text'}
        )

        self.fields['username'].widget.attrs.update(
            {'class': 'form-control form-control-xl', 'placeholder': 'eg : udith002', 'type':'text'}
        )

        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control form-control-xl', 'placeholder': '*************', 'type':'password'}
        )

        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control form-control-xl', 'placeholder': '*************', 'type':'password'}
        )


