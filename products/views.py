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
    return render(request, 'products/product_detail.html',context)



# 'new' 에서 작섣된 데이터를 'Article' 모델로로 저장해주는 함수
# 로그인이 되었을 때만 작동동
@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST,request.FILES) # 데이터 바인딩된 폼
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user  # 로그인된 유저를 작성자로 설정
            product.save()  # 저장
            # 다시 product_detail로로 redirect
            return redirect('products:product_detail',product.pk)
    else: 
        form = ArticleForm()

    context = {'form': form}
    return render(request,'products/create.html', context)




# article_detail의 데이터를 삭제하는 기능
# POST 방식일 때는 삭제하고
# GET 방식일 때는 삭제하지 않는 기능 필요
@require_POST  # request 값이 POST 일때만 동작
def delete(request,pk):
    if request.user.is_authenticated: # 로그인이 되어있을 때만 동작함함
            product = get_object_or_404(Product,pk=pk)
            product.delete()
            return redirect('products:products')
    return redirect('product:product_detail',pk)



# 흐름 
# article_detail '글 수정' 버튼 클릭시 
# 이때 request의 method는 GET 방식이기때문에에 
# form = ArticleForm(instance = article)
# 즉 form은 수정되지 않은 원본 상태 그래도 return을 해준다.
# update.html 로 이동
# update.html 에서 'Title', 'Content' 수정하고,
# '적용'버튼 클릭 시
# 'form action'으로 update 함수로 이동
# 이 경우 method="POST"로 전달되기때문에
# 변경이 가능한 상태로 전달됨
# 데이터가 수정된 상태로 form에 전달된후
# 유효성(is_valid) 검사후 유효하다면
# form.save() 저장을 해준다
# 그후 article_detail로 다시 이동
def update(request, pk):
    # article POST 방식이든 GET 방식이든 article을 조회해야하기때문에 일단 조회
    product = get_object_or_404(Product,pk=pk)
    if request.method == 'POST':
        # POST 방식이면 새로운 데이터를 집어 넣어 라는 명령어
        # 'instance = '의 값이 비워져있다면, 새로운 데이터를 만들어내는데
        #  instance=article 로 값을 채워준다면 article의 값을 수정해준다.
        # 이 코드는 update코드이기때문에 수정해줘야 하기에 instance=article코드를 사용용
        form = ArticleForm(request.POST, instance=product)
        # form 의 값이 유효하다면(is_valid) form을 저장해준다(form.save())
        if form.is_valid():
            product = form.save()
        return redirect('products:product_detail', product.pk)
    
    else:
        form = ArticleForm(instance = product)

    context = {'form': form, 'product': product}
    return render(request, 'products/update.html',context)



# 찜하기 기능
@login_required
def toggle_like(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.user in product.liked_by.all():
        # 이미 찜한 경우, 찜 해제
        product.liked_by.remove(request.user)
    else:
        # 찜하지 않은 경우, 찜 추가
        product.liked_by.add(request.user)

    return redirect('products:product_detail', product.pk)