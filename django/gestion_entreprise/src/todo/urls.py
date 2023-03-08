from django.urls import path

from .views import tasks_list, task_details, task_create, task_update, task_delete


urlpatterns = [
    path('list/', tasks_list, name="task-list"),
    path('create/', task_create, name="task-create"),
    path('details/<int:id>/', task_details, name="task-details"),
    path('update/<int:id>/', task_update, name="task-update"),
    path('delete/<int:id>/', task_delete, name="task-delete"),
]
