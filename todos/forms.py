from django.forms import ModelForm
from .models import Todo

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['todo']
    
    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)
        
        # self.fields['todo'].widget.attrs.update(
        #     {'class': 'form-control'}
        # )
