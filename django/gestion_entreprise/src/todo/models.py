from django.db import models

from datetime import date


class Task(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField()
    created_date = models.DateField(auto_now=True)
    due_date = models.DateField(default=date.today)
    closed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"({self.id}) {self.name}"
    
    def is_closed(self):
        return "Task is closed" if self.closed else "Task is open"
    
    def task_details(self):
        pass
        # Task due on due_date -> formatée : monday 05 september 2023
        # Task is closed