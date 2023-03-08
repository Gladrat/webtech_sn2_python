from django.shortcuts import render
from django.http import HttpResponse

def tasks_list(request):

    return render(request=request, template_name="todo/list.dj.html", context = {})

def task_details(request, id):
    context = {
        "title": "Task details",
        "id": id
    }
    return render(request=request, template_name="todo/details.dj.html", context=context)

def task_create(request):
    return render(request=request, template_name="todo/create.dj.html")

def task_update(request, id):
    return render(request=request, template_name="todo/update.dj.html")

def task_delete(request, id):
    return render(request=request, template_name="todo/delete.dj.html")
