from django.contrib.auth.forms import (
    UserChangeForm , 
    UserCreationForm,
    )
from django.contrib.auth import get_user_model
from django.urls import reverse
from django import forms
from .models import User  # 커스텀 사용자 모델

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User  # 커스텀 사용자 모델 사용
        fields = [
            'username', 
            #'email', 
            'password1', 
            'password2']




class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 우리가 알고있는 패스워드가 있다면
        if self.fields.get("password"):
            # 아래와 같이 도움을 주는 문구를 띄울께께
            password_help_text = (
                '<a href="{}">여기</a>'"를 누르기면 비밀번호 변경이 가능합니다"
            ).format(f"{reverse('accounts:change_password')}")
            self.fields["password"].help_text = password_help_text
