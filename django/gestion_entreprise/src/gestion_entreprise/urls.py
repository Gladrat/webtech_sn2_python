from django.contrib import admin
from django.urls import path, include
from django.views.defaults import server_error

urlpatterns = [
    path('', include('shared.urls')),
    path('admin/', admin.site.urls, name="admin"),
    path('error/', server_error, name="error"),
]
