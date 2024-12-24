from django.urls import path
from . import views


app_name = 'products'

urlpatterns = [
    path("index/", views.index, name="index"),
    # path("logout/", views.logout, name="logout"),

]