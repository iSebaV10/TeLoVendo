from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import CustomUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import LoginForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages


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

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Obtener las credenciales del formulario
            username = form.cleaned_data['nombre_de_usuario']
            password = form.cleaned_data['contraseña']
            print(username)
            print(password)

            # Autenticar al usuario
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Si el usuario es válido, inicia sesión y redirige a la página deseada
                auth_login(request, user)
                print('¡Inicio de sesión exitoso!')
                return redirect('index')  # Cambia 'index' por el nombre de la URL de la página de inicio
            else:
                # Si el usuario no es válido, muestra un mensaje de error en la página
                messages.error(request, 'Credenciales inválidas. Intente nuevamente.')
        else:
            # Si el formulario no es válido, imprime los errores y los datos ingresados
            print(form.errors)
            print(form.cleaned_data)
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('index')  # Reemplaza 'index' con el nombre de la URL de la página de inicio
