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

    path('users/', include('users.urls')),
    path('accounts/', include('accounts.urls')), 
    

]

# 디버그 모드, 즉 개발모드인 경우에는 아래의 코드를 실행하라는 명령어어
if settings.DEBUG:
    # 개발 모드 중 미디어 파일의 경로를 찾아주는 명령어
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)