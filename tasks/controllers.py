from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.db import IntegrityError
from .forms import TaskForm
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
                login(request, usuario)  # Asegúrate de usar `usuario` aquí
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
    # Cambia `user` a `usuario`
    tasks = Task.objects.filter(usuario=request.user, completado=False)  # Aquí se usa `usuario`
    return render(request, 'tasks.html', {'tasks': tasks, 'user': request.user})

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        # Asegúrate de que el nombre de usuario y contraseña se correspondan con el modelo User
        usuario = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if usuario is None:  # Cambia `user` a `usuario`
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrectos'
            })
        else:
            login(request, usuario)  # Usa `usuario` aquí
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
            new_task.usuario = request.user  # Cambia `user` a `usuario`
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
    task = Task.objects.get(pk=task_id)
    if request.method == 'GET':
        form = TaskForm(instance=task)
        return render(request, 'edit_task.html', {'task': task, 'form': form})
    else:
        try:
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'edit_task.html', {
                'task': task,
                'form': form,
                'error': 'Error en los datos'
            })
