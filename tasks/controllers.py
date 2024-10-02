from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.db import IntegrityError
from .forms import TaskForm, CustomAuthenticationForm
from .models import Task

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                usuario = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                usuario.save()
                login(request, usuario)  
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })

        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Las contraseñas no coinciden'
        })

def tasks(request):
    tasks = Task.objects.filter(usuario=request.user, completado=False) 
    return render(request, 'tasks.html', {'tasks': tasks, 'user': request.user})

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': CustomAuthenticationForm()
        })
    else:
        
        usuario = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if usuario is None:  
            return render(request, 'signin.html', {
                'form': CustomAuthenticationForm(),
                'error': 'Usuario o contraseña incorrectos'
            })
        else:
            login(request, usuario)  
            return redirect('tasks')

def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form': TaskForm
        })
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.usuario = request.user  
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_task.html', {
                'form': TaskForm,
                'error': 'Error en los datos'
            })

def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'task_detail.html', {'task': task})

def complete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.completado = True
    task.save()
    return redirect('tasks')

def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('tasks')

def edit_task(request, task_id):
    # Obtenemos la tarea por ID, si no existe retorna un error 404
    task = get_object_or_404(Task, pk=task_id, usuario=request.user)
    
    if request.method == 'GET':
        # Si es una solicitud GET, cargamos el formulario con los datos de la tarea actual
        form = TaskForm(instance=task)
        return render(request, 'edit_task.html', {'form': form, 'task': task})
    else:
        try:
            # Si es una solicitud POST, guardamos los nuevos datos
            form = TaskForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return redirect('tasks')
            else:
                return render(request, 'edit_task.html', {'form': form, 'task': task, 'error': 'Datos no válidos'})
        except ValueError:
            return render(request, 'edit_task.html', {'form': form, 'task': task, 'error': 'Error en los datos'})

