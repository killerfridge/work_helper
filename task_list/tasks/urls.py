from django.urls import path
from .views import (
    TaskListView,
    TaskDetailView,
    OwnerListView,
    OwnerDetailView,
    index,
    SubTaskDetailView,
    PersonDetailView,
)

app_name = 'tasks'
urlpatterns = [
    path('', index, name='index'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/<int:pk>', TaskDetailView.as_view(), name='task-detail'),
    path('owners/', OwnerListView.as_view(), name='person-list'),
    path('owners/<int:pk>', PersonDetailView.as_view(), name='person-detail'),
    path('subtasks/<int:pk>', SubTaskDetailView.as_view(), name='subtask-detail')
]