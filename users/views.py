from django.shortcuts import render
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST,require_http_methods


def users(reqeust):
    return render(reqeust, 'users.html')

@login_required
def profile(request, username):
    # 현재 로그인한 유저가 찜한 상품을 가져옴
    liked_products = request.user.liked_products.all() 
    context = {
    'username': username,
    'liked_products': liked_products,
    }
    return render(request, "users/profile.html",context)
# Create your views here.
