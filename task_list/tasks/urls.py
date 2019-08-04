from django.urls import path
from .views import TaskListView, TaskDetailView, OwnerListView, OwnerDetailView, index

app_name = 'tasks'
urlpatterns = [
    path('', index, name='index'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/<int:pk>', TaskDetailView.as_view(), name='task-detail'),
    path('owners/', OwnerListView.as_view(), name='person-list'),
    path('owners/<int:pk>', OwnerDetailView.as_view(), name='person-detail')
]