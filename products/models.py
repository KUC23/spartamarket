from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.


class  Product(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
                                    #auto_now_add 새로 추가될 때 작성   
    created_at = models.DateTimeField(auto_now_add=True)
                                    # auto_now 추가 될 때 마다 작성성
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', blank=True)   # text 테이터에는 null = True를 주지 않을 것을 권장하고있다.
    # 찜하기 기능
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="liked_products", blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products', null=True, blank=True)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    article = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content