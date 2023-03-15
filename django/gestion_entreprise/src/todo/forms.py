from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name", "description", "due_date", "category", "tag"]
        labels = {"name":"Task name"}
        widgets = {
            "due_date": forms.SelectDateWidget(),
            "tag": forms.CheckboxSelectMultiple()
        }

# RTFM !