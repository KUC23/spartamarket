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
# from .forms import CustomUserChangeForm


@require_http_methods(['GET','POST'])
def login(request):
    pass