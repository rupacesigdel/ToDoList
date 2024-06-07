from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from home.models import Task
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def my_view(request):
    return render(request, 'my_template.html')


# Create your views here.
def home(request):
    context = {'success': False, 'name' :'Rupesh'}
    if request.method == "POST":
        # handel the form
        title = request.POST['title']
        desc = request.POST['desc']
        print(title, desc)
        ins = Task(taskTitle=title, taskDesc=desc)
        ins.save()
        context = {'success': True}

    return render(request, 'index.html', context)

def task(request):
    allTasks = Task.objects.all()
    # print(allTasks)
    # for item in allTasks:
    #     print(item.taskTitle)
    context = {'task': allTasks}
    return render(request, 'task.html', context)

def search(request):
    query = request.GET.get('q')
    if query:
        results = Task.objects.filter(taskTitle__icontains=query)  | Task.objects.filter(taskDesc__icontains=query) # replace with actual field
    else:
        results = Task.objects.none()
    
    return render(request, 'search_results.html', {'results': results})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    request.session['deleted_task'] = {
        'id': task.id,
        'title': task.taskTitle,
        'desc': task.taskDesc,
    }
    task.delete()
    messages.success(request, 'Task deleted! <a href="/undo_delete/">Undo</a>', extra_tags='safe')
    return redirect('/task')

@login_required
def undo_delete(request):
    deleted_task = request.session.pop('deleted_task', None)
    if deleted_task:
        Task.objects.create(
            id=deleted_task['id'],
            taskTitle=deleted_task['title'],
            taskDesc=deleted_task['desc'],
        )
        messages.success(request, 'Task restored!')
    else:
        messages.error(request, 'No task to restore.')
    return redirect('/task')

@login_required
def edit_task(request, pk):  # Change 'task_id' to 'pk'
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        # Handle form submission for editing task
        title = request.POST['title']
        desc = request.POST['desc']
        task.taskTitle = title
        task.taskDesc = desc
        task.save()
        messages.success(request, 'Task updated successfully!')
        return redirect('/task')
    else:
        context = {'task': task}
        return render(request, 'edit_task.html', context)
