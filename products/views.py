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



# 'new' 에서 작섣된 데이터를 'Article' 모델로로 저장해주는 함수
# 로그인이 되었을 때만 작동동
@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST,request.FILES) # 데이터 바인딩된 폼
        if form.is_valid():
            # 데이터를 저장하고,
            product = form.save()
            # 다시 product_detail로로 redirect
            return redirect('product_detail',product.pk)
    else: 
        form = ArticleForm()

    context = {'form': form}
    return render(request,'create.html', context)