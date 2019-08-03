from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Task, Department, Owner, Stakeholder


# Register your models here.
@admin.register(Task)
class AdminTask(ModelAdmin):
    list_display = ('title', 'owner', 'start_by', 'overdue')
    list_filter = ('due_date', 'owner')


@admin.register(Owner)
class AdminOwner(ModelAdmin):
    pass


@admin.register(Department)
class AdminDepartment(ModelAdmin):
    pass


@admin.register(Stakeholder)
class AdminStakeholder(ModelAdmin):
    pass
