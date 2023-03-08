from django.shortcuts import render
from django.http import HttpResponse

def tasks_list(request):
    return render(request=request, template_name="todo/tasks_list.dj.html")

def task_details(request, id):
    # return HttpResponse(f"<h1>Task details ({id}) :</h1>")
    pass