from django.db import models
from users.models import Profile
import uuid

class Thought(models.Model):
    author = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    content = models.TextField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.content)
