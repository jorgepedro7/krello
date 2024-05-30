from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from tasks.models import Task, Column
from tasks.forms import TaskForm, ColumnForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'tasks'
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['columns'] = Column.objects.filter(user=self.request.user)
        context['task_form'] = TaskForm()
        context['column_form'] = ColumnForm()
        return context

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'add_task.html'
    form_class = TaskForm
    success_url = reverse_lazy('task-list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        column_id = self.request.POST.get('column')
        if column_id:
            form.instance.column_id = column_id
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'edit_task.html'
    fields = ['title', 'description', 'status', 'column']
    success_url = reverse_lazy('task-list')
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ColumnCreateView(LoginRequiredMixin, CreateView):
    model = Column
    template_name = 'add_column.html'
    fields = ['name']
    success_url = reverse_lazy('task-list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)   

class ColumnUpdateView(LoginRequiredMixin, UpdateView):
    model = Column
    template_name = 'edit_column.html'
    fields = ['name']
    success_url = reverse_lazy('task-list')

    def get_queryset(self):
        return Column.objects.filter(user=self.request.user)

@method_decorator(csrf_exempt, name='dispatch')
class UpdateTaskStatusView(View):
    def post(self, request, task_id):
        data = json.loads(request.body)
        new_column_id = data.get('column')

        try:
            task = Task.objects.get(id=task_id, user=request.user)
            task.column_id = new_column_id
            task.save()
            return JsonResponse({'success': True})
        except Task.DoesNotExist:
            return JsonResponse({'error': 'Task not found'}, status=404)
