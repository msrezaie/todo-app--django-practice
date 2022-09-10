from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . models import Task

class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'base/list.html'

class TaskDetail(DetailView):
    model = Task
    template_name = 'base/detail.html'

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    context_object_name = 'tasks'
    template_name = 'base/create.html'
    success_url = reverse_lazy('task-list')