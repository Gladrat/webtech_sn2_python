from django.urls import path

from .views import tasks_list, task_details, task_create, task_update, task_delete, task_slug

urlpatterns = [
    path('', tasks_list, name="task-list"),
    path('create/', task_create, name="task-create"),
    path('details/<int:id>/', task_details, name="task-details"),
    path('<slug:slug>/', task_slug, name="task-slug"),
    path('update/<int:id>/', task_update, name="task-update"),
    path('delete/<int:id>/', task_delete, name="task-delete"),
    # path('filter/<str:tag>', task_filter_tag, name="task-filter-tag")
]
