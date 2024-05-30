from django.db import models
from django.contrib.auth.models import User

class Column(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS_CHOICES = [
        ('A fazer', 'A fazer'),
        ('Em andamento', 'Em andamento'),
        ('Concluído', 'Concluído'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='A fazer')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    column = models.ForeignKey(Column, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title
