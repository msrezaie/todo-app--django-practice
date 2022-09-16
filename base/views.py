from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from . models import Task

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'base/list.html'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'base/detail.html'

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    template_name = 'base/create.html'
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    context_object_name = 'tasks'
    template_name = 'base/update.html'
    success_url = reverse_lazy('task-list')

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'base/delete.html'
    success_url = reverse_lazy('task-list')