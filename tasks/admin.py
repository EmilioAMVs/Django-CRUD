from django.contrib import admin
from .models import Task

class taskAdmin(admin.ModelAdmin):
    readonly_fields = ('creado',)
    
# Register your models here.
admin.site.register(Task, taskAdmin)
