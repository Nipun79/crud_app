from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.create,name="create"),
    path('task_delete/<str:pk>/',views.task_delete,name="task_delete"),
     path('task_edit/<str:pk>/',views.task_edit,name="task_edit")
]
