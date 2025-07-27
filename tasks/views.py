from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Task, Category
from .forms import TaskForm

# Create your views here.


def index(request):
    """View to display all tasks on the index page."""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task added successfully!')
            return redirect('tasks:index')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = TaskForm()
    
    tasks = Task.objects.all().order_by('due_date', '-created_at')
    categories = Category.objects.all()
    
    context = {
        'tasks': tasks,
        'categories': categories,
        'form': form,
    }
    
    return render(request, 'tasks/index.html', context)


@require_POST
@csrf_exempt
def toggle_task(request, task_id):
    """Toggle the completion status of a task."""
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    
    return JsonResponse({
        'success': True,
        'completed': task.completed,
        'task_id': task.id
    })


@require_POST
@csrf_exempt
def delete_task(request, task_id):
    """Delete a task."""
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    
    return JsonResponse({
        'success': True,
        'task_id': task_id
    })
