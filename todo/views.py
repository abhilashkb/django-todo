from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Task, TaskDate
from datetime import date

@login_required
def list_tasks(request):
    """
    Lists all tasks and their status for a given date. If a task doesn't have a status
    for the given date, it will be created. The view will also render a calendar
    component to facilitate the selection of the date.

    :param request: The request object.
    :return: A rendered HTML page with the list of tasks and their status for the
             given date.
    """
    selected_date = request.GET.get('date', date.today().isoformat())
    tasks = Task.objects.filter(user=request.user)
    task_dates = TaskDate.objects.filter(task__user=request.user, date=selected_date)

    # Initialize tasks in TaskDate model if they don't exist for the selected date
    for task in tasks:
        if not TaskDate.objects.filter(task=task, date=selected_date).exists():
            TaskDate.objects.create(task=task, date=selected_date)

    task_dates = TaskDate.objects.filter(task__user=request.user, date=selected_date)
    return render(request, 'list_tasks.html', {'tasks': task_dates, 'selected_date': selected_date})

@login_required
def create_task(request):
    """
    A view to create a new task.

    :param request: The request object
    :return: A rendered HTML page with a form to create a new task
    """
    if request.method == 'POST':
        title = request.POST.get('title')
        Task.objects.create(title=title, user=request.user)
    return render(request, 'create_task.html')


@login_required
def toggle_task_status(request, task_id):
    task_date = get_object_or_404(TaskDate, id=task_id, task__user=request.user)
    if request.method == 'POST':
        task_date.completed = not task_date.completed
        task_date.save()
    return redirect('list_tasks')

def custom_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return redirect('list_tasks')



