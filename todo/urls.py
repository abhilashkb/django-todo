from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.list_tasks, name='list_tasks'),
    path('create/', views.create_task, name='create_task'),
    path('toggle/<int:task_id>/', views.toggle_task_status, name='toggle_task_status'),
    path('accounts/login/', include('django.contrib.auth.urls')),
    path('accounts/logout/', views.custom_logout, name='logout'),  # Use custom logout view
]