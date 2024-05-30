from django.contrib import admin
from django.urls import path
from tasks.views import TaskListView, TaskUpdateView, UpdateTaskStatusView, ColumnCreateView, TaskCreateView, ColumnUpdateView
from accounts.views import RegisterView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TaskListView.as_view(), name='task-list'),
    path('new/', TaskCreateView.as_view(), name='add_task'),
    path('<int:pk>/edit/', TaskUpdateView.as_view(), name='edit_task'),
    path('add_column/', ColumnCreateView.as_view(), name='add_column'),
    path('edit_column/', ColumnUpdateView.as_view(), name='edit_column'),
    path('update-task-status/<int:task_id>/', UpdateTaskStatusView.as_view(), name='update_task_status'),

    # URLs de autenticação
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/register/', auth_views.LoginView.as_view(template_name='register.html'), name='register'),
]





