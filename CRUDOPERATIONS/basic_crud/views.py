from django.shortcuts import redirect, render
from . models import task_create
# Create your views here.
def create(request):
    if request.method == "GET":
        tasks=task_create.objects.all()
        return render(request,'home.html',{'tasks':tasks})
    else:
        task_name= request.POST.get("create-task-name")
        task_create.objects.create(name=task_name,completed=False)
        return redirect("/")
def  task_delete(request,pk):
    task=task_create.objects.get(id=pk)
    task.delete()
    return redirect("/")
def task_edit(request,pk):
    if request.method == "POST":
        task=task_create.objects.get(id=pk)
        return render(request,'edit.html',{'task':task})
    else:
        task_name= request.GET.get("create-task-name")
        task=task_create.objects.get(id=pk)
        task.name=task_name
        task.save()
        return redirect("/")