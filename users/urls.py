from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerUser, name='register'),

    path('users/', views.profiles, name='profiles'),
    path('profile/<str:pk>/', views.userProfile, name='user-profile'),
    path('user/account/', views.userAccount, name='account'),
    path('user/analytics/', views.userAnalytics, name='analytics'),
    
    path('user/update-profile/', views.updateProfile, name='update-profile'),
    
    path('user/add-skill/', views.addSkill, name='add-skill'),
    path('user/update-skill/<str:pk>', views.updateSkill, name='update-skill'),
    path('user/delete-skill/<str:pk>', views.deleteSkill, name='delete-skill'),
    
]