from django.db import models
import uuid
from users.models import Profile
from todos.models import Todo

class Note(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200, null=True, blank=True)
    todo_field = models.ManyToManyField(Todo, blank=True)
    description = models.TextField(max_length=50000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.title)
    
    class Meta:
        ordering = ['-created']
