from django.urls import path
from . import views


app_name = 'users'

urlpatterns = [
    path('', views.users, name='users'),
    path("profile/<str:username>/", views.profile, name= 'profile'),
    path('profile/<str:username>/toggle_follow/', views.toggle_follow, name='toggle_follow'),
]