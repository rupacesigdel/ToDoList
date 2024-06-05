from django.shortcuts import render, HttpResponse
from home.models import Task
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