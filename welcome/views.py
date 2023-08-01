from django.shortcuts import render
from .models import CustomUser

def index(request):
    return render(request, 'index.html')

def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'user_list.html',{
        'users': users
    })