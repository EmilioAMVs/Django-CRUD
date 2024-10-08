"""
URL configuration for djangocrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import controllers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', controllers.home, name='home'),
    path('signup/', controllers.signup,name='signup'),
    path('tasks/', controllers.tasks, name='tasks'),
    path('tasks/create/', controllers.create_task, name='create_task'),
    path('tasks/detail/<int:task_id>/', controllers.task_detail, name='task_detail'),
    path('tasks/complete/<int:task_id>/', controllers.complete_task, name='complete_task'),
    path('tasks/delete/<int:task_id>/', controllers.delete_task, name='delete_task'),
    path('taskks/edit/<int:task_id>/', controllers.edit_task, name='edit_task'),
    path('signout/', controllers.signout, name='signout'),
    path('signin/', controllers.signin, name='signin'), 
]
