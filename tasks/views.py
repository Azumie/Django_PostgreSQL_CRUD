from django.shortcuts import render, redirect
from .models import Task
# Create your views here.
# va a intentar renderizar un archivo, pero cuando ocurra algo. Para ello creamos un archivo llamado url
def list_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'list_tasks.html', {'tasks': tasks})

def create_task(request):
    task = Task(title=request.POST['title'], description=request.POST['description'])
    task.save()
    print(request.POST) 
    return redirect('/tasks/')