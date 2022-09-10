from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskList.as_view(), name='task-list'),
    path('task-detail/<int:pk>', views.TaskDetail.as_view(), name='task-detail'),
    path('task-create/', views.TaskCreate.as_view(), name='task-create')
]