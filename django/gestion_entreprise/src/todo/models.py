from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.html import format_html
from django.contrib import admin

from datetime import date

# Category
    # name
    # slug
class Category(models.Model):
    name = models.CharField(max_length=50, blank=False)
    slug = models.SlugField(null=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"({self.id}) {self.name}"


class Tag(models.Model):
    name = models.CharField(max_length=50, blank=False)
    slug = models.SlugField(null=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"({self.id}) {self.name}"


class Task(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField(Tag)
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField()
    created_date = models.DateField(auto_now=True)
    due_date = models.DateField(default=date.today)
    closed = models.BooleanField(default=False)
    slug = models.SlugField(null=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        if not self.category:
            self.category = Category.objects.order_by('id').first()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"({self.id}) {self.name}"
    
    def is_closed(self):
        return "Task is closed" if self.closed else "Task is open"
    
    def task_details(self):
        str_closed = f"due on {self.due_date.strftime('%a %d %b %Y')}" if not self.closed else "closed"
        return f"The task {self.name} is {str_closed}"

    @admin.display(description="Due date")
    def colored_due_date(self):    
        today = date.today()
        delta = (self.due_date - today).days
        color = "red"
        if delta >= 7:
            color = "green"
        elif delta > 0:
            color = "orange"
        return format_html(f"<span style='color:{color}'>{self.due_date.__format__('%d %B %Y')}</span>")
    
    def shortened_description(self):
        return f"{self.description[:20]}..." if len(self.description) > 20 else self.description

    def get_absolute_url(self):
        return reverse("task-slug", kwargs={"slug": self.slug})
    
    class Meta:
        ordering = ['slug']
        verbose_name = "Tâche"


class Dice:
    
    def __init__(self, faces):
        self.faces = faces
        
    def roll(self):
        return self.faces