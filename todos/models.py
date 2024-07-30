from django.db import models
import uuid
from users.models import Profile

class Todo(models.Model):
    STATUS = (
        (1, 'Pending'),
        (2, 'Done')
    )
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    todo = models.CharField(max_length=200, null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=1)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.todo)
