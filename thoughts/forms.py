from django.forms import ModelForm
from django import forms
from .models import Thought

class ThoughtForm(forms.ModelForm):
    class Meta:
        model = Thought
        fields = ['content']
    
    def __init__(self, *args, **kwargs):
        super(ThoughtForm, self).__init__(*args, **kwargs)

        self.fields['content'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Thought'},
        )