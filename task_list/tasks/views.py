from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Task, Department, Owner, Stakeholder


# Create your views here.
class TaskListView(ListView):
    model = Task


class TaskDetailView(DetailView):
    model = Task


class OwnerDetailView(DetailView):
    model = Owner


class OwnerListView(ListView):
    model = Owner


def index(request):
    return render(request, 'tasks/index.html')
