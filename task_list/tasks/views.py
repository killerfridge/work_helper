from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Task, Department, Owner, Stakeholder, Person


# Create your views here.
class TaskListView(ListView):
    model = Task


class TaskDetailView(DetailView):
    model = Task


class OwnerDetailView(DetailView):
    model = Person


class OwnerListView(ListView):
    model = Person

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)


def index(request):
    return render(request, 'tasks/index.html')
