from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.todoList, name='todos')
]