from django.contrib import admin
from tasks.models import Task, Column
from django.contrib.admin.sites import site


if site.is_registered(Task):
    admin.site.unregister(Task)
if site.is_registered(Column):
    admin.site.unregister(Column)

# Registre os modelos
admin.site.register(Task)
admin.site.register(Column)