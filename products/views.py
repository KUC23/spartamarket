from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .models import Product
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST,require_http_methods



def index(request):
    return render(request, 'products/index.html')

def products(request):
    products = Product.objects.all().order_by('-created_at')
    context = {
        "products": products,

    }
    return render(request, 'products/products.html',context)


def product_detail(request, pk):
    product = get_object_or_404(Product,pk=pk)
    context = {'product' : product}
    return render(request, 'product_detail.html',context)

