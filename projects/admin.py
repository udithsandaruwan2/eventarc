from django.contrib import admin

from .models import Project, Like, Tag

# Register your models here.

admin.site.register(Project)
admin.site.register(Like)
admin.site.register(Tag)

