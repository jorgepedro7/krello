from django import forms
from .models import Task, Column

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'column']

class ColumnForm(forms.ModelForm):
    class Meta:
        model = Column
        fields = ['name']
