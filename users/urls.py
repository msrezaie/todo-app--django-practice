from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('task-login/', views.TaskLoginView.as_view(), name='task-login'),
    path('task-logout/', LogoutView.as_view(next_page='task-login'), name='task-logout')
]