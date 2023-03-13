from django.shortcuts import render
from django.http import HttpResponse

from .models import Task

def tasks_list(request):
    tasks = Task.objects.all()
    # print(tasks[0])
    return render(request=request, template_name="todo/list.dj.html", context = {'tasks':tasks})

def task_details(request, id):
    task = Task.objects.get(id=id)
    context = {"task":task}
    # print(task)
    return render(request=request, template_name="todo/details.dj.html", context=context)

def task_create(request):
    return render(request=request, template_name="todo/create.dj.html")

def task_update(request, id):
    return render(request=request, template_name="todo/update.dj.html")

def task_delete(request, id):
    return render(request=request, template_name="todo/delete.dj.html")
