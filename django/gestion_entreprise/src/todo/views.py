from django.shortcuts import render
from django.http import HttpResponse

from .models import Task

def tasks_list(request):
    task_list = Task.objects.all()
    context = {
        "task_list":task_list,
        "name": "Geoffroy",
        "age": 38,
        "var": False,
        "hobbies": ["coder", "gamer", "elever un enfant"]
    }
    return render(request=request, template_name="todo/list.dj.html", context=context)

def task_slug(request, slug):
    task = Task.objects.get(slug=slug)
    context = {
        "task":task
    }
    return render(request=request, template_name="todo/details.dj.html", context=context)

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
