from django.shortcuts import render,redirect
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserChangeForm,
    UserCreationForm,
    PasswordChangeForm,
)
from django.contrib.auth import (
    login as auth_login,
    logout as auth_logout,
    update_session_auth_hash,
)
from django.views.decorators.http import require_POST,require_http_methods
from .forms import (
    CustomUserCreationForm, 
    CustomUserChangeForm,
)

# AuthenticationForm: Django에서 제공하는 로그인 폼을 처리하는 기본적인 클래스 
#                     이 폼은 사용자가 로그인할 때 아이디와 비밀번호를 입력받고, 
#                     해당 정보가 올바른지 확인하는 역할
# auth_login 로그인상태를 유지시켜주는 역할
# require_http_methods(['GET','POST']) 'GET','POST'이외의 모든것을 쳐냄
@require_http_methods(['GET','POST'])
def login(request):
    if request.method == 'POST':
        # 아이디와 비밀번호를 확인
        form = AuthenticationForm(data=request.POST)
        # form의 형태가 유효하다면면
        if form.is_valid():
            # 로그인상태를 유지시켜줌줌
            auth_login(request,form.get_user())
            # 로그인 한 후에 기본에 있던 페이지에 있을지 인덱스로 돌아갈지 정함함
            next_url = request.GET.get('next') or '/products/index'
    else:
        # 로그인이 'POST' 형식이 아니라면 빈 form을 돌려줌
        form = AuthenticationForm()
    context = {'form': form }
    return render(request, 'accounts/login.html',context)



# 'POST' 이외의 값을 모두 쳐내주는 데코레이트
@require_POST
def logout(request):
    # user가 로그인 상태일 때 사용가능함함
    if request.user.is_authenticated:
        # 로그 아웃 동작후
        auth_logout(request)
    # index로 돌아감
    return redirect('/products/index')




# UserCreationForm : Django에서 기본으로 제공하는 회원가입 폼
# 새로운 계정을 만들 때 필요한 기본적인 입력 필드와 유효성 검사를 자동으로 제공
# require_http_methods(['GET','POST']) 'GET','POST'이외의 모든것을 쳐냄
@require_http_methods(['POST','GET'])
def signup(request):
    if request.method == 'POST':
        # POST 형식인 request의 필드와 유효성 검사 
        form = CustomUserCreationForm(request.POST)
        # form 값의 유효성 검사
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('/products/index')
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/signup.html',context)


# 회원 탈퇴
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('index')



# 회원정보 수정
@require_http_methods(['GET','POST'])
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CustomUserChangeForm(instance = request.user)
    context = {'form' : form}  
    return render(request,'accounts/update.html',context)


@require_http_methods(["GET", "POST"])
def change_password(request):
    if request.method == 'POST':
        # 순서가 중요
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            # 비밀번호를 변경한 후 에 로그인을 유지해줌
            update_session_auth_hash(request, form.user)
            return redirect('index')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form':form}
    return render(request,'accounts/change_password.html',context)




