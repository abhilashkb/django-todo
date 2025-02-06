from django.shortcuts import render
from .models import Task
# Create your views here.

def list_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'todo/list_tasks.html', {'tasks': tasks})

def create_task(request):
    return render(request, 'todo/create_task.html') 

def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'todo/update_task.html', {'task': task})