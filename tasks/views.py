from django.shortcuts import render, redirect

# Create your views here.
# va a intentar renderizar un archivo, pero cuando ocurra algo. Para ello creamos un archivo llamado url
def list_tasks(request):
    return render(request, 'list_tasks.html')

def create_task(request):
    print(request.POST)
    return redirect('/tasks/')