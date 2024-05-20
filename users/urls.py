from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerUser, name='register'),

    path('', views.profiles, name='profiles'),
    path('profile/<str:pk>/', views.userProfile, name='user-profile'),
    path('account/', views.userAccount, name='account'),
    path('user/analytics', views.userAnalytics, name='analytics'),
]