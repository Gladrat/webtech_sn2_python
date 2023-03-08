from django.urls import path

from .views import tasks_list, task_details, task_list_created_by_date


urlpatterns = [
    path('', tasks_list, name="task-list"),
    path('details/<int:id>/', task_details, name="task-list"),
]
