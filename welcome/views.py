from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import CustomUserForm

def index(request):
    return render(request, 'index.html')

def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'user_list.html',{
        'users': users
    })

def create_user(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = CustomUserForm()
    return render(request, 'create_user.html', {'form': form})