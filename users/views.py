from django.shortcuts import render
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST,require_http_methods
from accounts.models import User

# 유저가 등록한 물품과 찜한 물품 정보를 가져오기 위해 필요
from products.models import Product  

def users(reqeust):
    return render(reqeust, 'users.html')

@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    # 유저가 등록한 물품
    products_registered = Product.objects.filter(owner=user) 
    # 현재 로그인한 유저가 찜한 상품을 가져옴
    liked_products = request.user.liked_products.all()
    # 팔로우 여부 
    is_following = request.user in user.followers.all()  
    context = {
    'username': username,
    'liked_products': liked_products,
    'is_following': is_following,
    'products_registered': products_registered,

    }
    return render(request, "users/profile.html",context)
# Create your views here.

@login_required
def toggle_follow(request, username):
    target_user = get_object_or_404(User, username=username)
    
    if request.user in target_user.followers.all():
        target_user.followers.remove(request.user)
    else:
        target_user.followers.add(request.user)
    return redirect('users:profile', username=target_user.username)
