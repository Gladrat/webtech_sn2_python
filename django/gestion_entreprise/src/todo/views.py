from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Task, Tag
from .forms import TaskForm

def tasks_list(request):
    task_list = Task.objects.all()
    tag_list = Tag.objects.all()
    context = {
        "task_list":task_list,
        "tag_list":tag_list
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
    saved = False
    if (request.method == "POST"):
        form = TaskForm(request.POST)
        if form.is_valid:
            task = form.save(commit=False)
            # manipulation des données du formulaire
            # ...
            task.save()
            saved = f"The task {form.cleaned_data.get('name')} was created"
            return HttpResponseRedirect(request.path)
    else:
        form = TaskForm()
    return render(request=request, template_name="todo/create.dj.html", context={"form":form, "saved":saved})

def task_update(request, id):
    return render(request=request, template_name="todo/update.dj.html")

def task_delete(request, id):
    t = Task.objects.get(id=id)
    t.delete()
    return render(request=request, template_name="todo/delete.dj.html")
