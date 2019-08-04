from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Task, Department, Owner, Stakeholder, Person, SubTask


# Register your models here.
class SubTaskInline(admin.TabularInline):
    model = SubTask
    extra = 0


@admin.register(Task)
class AdminTask(ModelAdmin):
    list_display = ('title', 'owner', 'start_by', 'overdue')
    list_filter = ('due_date', 'owner')
    inlines = [SubTaskInline]

    fieldsets = (
        (
            None, {
                'fields': ('title', 'description')
            }
        ),
        (
          'Owners', {
              'fields': ('owner', 'stakeholders')
          }
        ),
        (
            'Due', {
                'fields': ('due_date', 'duration_days', 'duration_hours', 'duration_minutes')
            }
        )
    )


@admin.register(Owner)
class AdminOwner(ModelAdmin):
    pass


@admin.register(Department)
class AdminDepartment(ModelAdmin):
    pass


@admin.register(Stakeholder)
class AdminStakeholder(ModelAdmin):
    pass


@admin.register(Person)
class AdminStakeholder(ModelAdmin):
    pass


@admin.register(SubTask)
class AdminSubTask(ModelAdmin):
    pass


