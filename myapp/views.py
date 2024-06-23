# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import render

# Create your views here.
def index(request):
    title = 'Django course!!'
    return render(request, 'index.html', {
        'title':title
    })

def about(request):
    return request(request, 'about.html')

def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'projects':projects
    })

def tasks(request):
    #usamos % para concatenar
    #task = Task.objects.get(Task)
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {
        'tasks':tasks
    })