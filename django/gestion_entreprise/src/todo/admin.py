from django.contrib import admin

from .models import Task

# admin.site.register(Task)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['slug', 'name', 'shortened_description', 'closed', 'colored_due_date', 'created_date', 'get_absolute_url']
    search_fields = ['name__startswith', 'description__contains']
    date_hierarchy = 'due_date'
    list_filter = ['closed', 'due_date', 'created_date']
    empty_display_value = '-'
    list_editable = ['closed']
    list_display_links = ['slug']
    list_per_page = 10