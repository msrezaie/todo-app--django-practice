from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('task-list/', views.TaskList.as_view(), name='task-list'),
    path('task-detail/<int:pk>', views.TaskDetail.as_view(), name='task-detail'),
    path('task-create/', views.TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>', views.TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>', views.TaskDelete.as_view(), name='task-delete'),

    path('', RedirectView.as_view(url='task-list/'))
]