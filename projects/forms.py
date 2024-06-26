from django.forms import ModelForm
from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image', 'description', 'demo_link', 'source_link', 'tags']

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Title'}
        )

        self.fields['featured_image'].widget.attrs.update(
            {'class': 'form-control', 'id':'formFile'}
        )

        self.fields['description'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Description'}
        )

        self.fields['source_link'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Demo Link'}
        )

        self.fields['demo_link'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Source Link'}
        )

        self.fields['tags'].widget.attrs.update({
            'class': 'choices form-select',
            'multiple': 'multiple'
        })

