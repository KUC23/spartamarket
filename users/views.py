from django.shortcuts import render

def users(reqeust):
    return render(reqeust, 'users.html')


def profile(request, username):
    context = {
    'username': username
    }
    return render(request, "profile.html",context)
# Create your views here.
