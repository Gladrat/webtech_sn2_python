from django.shortcuts import render
from django.http import HttpResponse

from .forms import SignupForm


def index(request):
    return render(request=request, template_name="shared/index.dj.html")
    # return HttpResponse("<h1>Hello world of Django !</h1>")

def about(request):
    return render(request=request, template_name="shared/about.dj.html")
    # return HttpResponse("<h1>Hello world of about !</h1>")
    
def register(request):
    if (request.method == "POST"):
        form = SignupForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        else:
            print(form.errors)
    else:
        form = SignupForm()
    
    return render(request=request, template_name="shared/register.dj.html", context={"form":form})