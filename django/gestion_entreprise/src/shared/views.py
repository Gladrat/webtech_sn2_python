from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request=request, template_name="shared/index.dj.html")
    # return HttpResponse("<h1>Hello world of Django !</h1>")

def about(request):
    return render(request=request, template_name="shared/about.dj.html")
    # return HttpResponse("<h1>Hello world of about !</h1>")