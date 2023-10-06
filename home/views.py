from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def home(request):
    if request.method != "POST":
        tasks = Task.objects.filter(is_completed=False)
        completed_tasks = Task.objects.filter(is_completed=True)
        return render(request, 'home.html', {'tasks': tasks, 'completed_tasks': completed_tasks})
    else:
        task = request.POST['task']
        Task.objects.create(task = task)
        return redirect('home')


def mark_as_done(request, task_id):
    task = get_object_or_404(Task, id=task_id)  # Get the task or return 404 if not found
    task.is_completed = True  # Set is_completed to True
    task.save()  # Save the changes
    return redirect('home')  # Redirect to the home view or wherever you like


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)  # Get the task or return 404 if not found
    task.delete()  # Save the changes
    return redirect('home')  # Redirect to the home view or wherever you like

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'POST':
        new_task_content = request.POST['task']
        task.task = new_task_content
        task.save()
        return redirect('home')

    return render(request, 'edit_task.html', {'task': task})