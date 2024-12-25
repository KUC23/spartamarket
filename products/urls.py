from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'products'

urlpatterns = [
    path("index/", views.index, name="index"),
    path("", views.products, name="products"),
    path('create/', views.create, name = 'create'),
    path("<int:pk>/", views.product_detail, name="product_detail"),
    path('<int:pk>/delete/',views.delete, name = 'delete'),
    path('<int:pk>/update/',views.update, name = 'update'),
    path('like/<int:pk>/', views.toggle_like, name='toggle_like'),

    path('users/', include('users.urls')),
    path('accounts/', include('accounts.urls')), 
    

]

