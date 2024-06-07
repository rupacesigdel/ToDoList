from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('task/', views.task, name='task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('undo_delete/', views.undo_delete, name='undo_delete'),
    path('task/<int:pk>/edit/', views.edit_task, name='edit_task'),


]
