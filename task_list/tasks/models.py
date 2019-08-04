from django.db import models
from django.urls import reverse
import datetime as dt


# Create your models here.
class AbstractTask(models.Model):
    title = models.CharField(max_length=150, help_text='Task Name')
    owner = models.ForeignKey('Owner', null=False, blank=False, on_delete=models.CASCADE)

    description = models.TextField(blank=True, null=True)

    duration_days = models.IntegerField(default=0, null=True, blank=True)
    duration_hours = models.IntegerField(default=0, null=True, blank=True)
    duration_minutes = models.IntegerField(default=0, null=True, blank=True)

    due_date = models.DateTimeField(blank=False, null=False)

    started = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)

    @property
    def start_by(self):
        seconds = float((self.duration_hours*3600) + (self.duration_minutes * 60))
        return self.due_date - dt.timedelta(
            days=float(self.duration_days), seconds=seconds
        )

    @property
    def overdue(self):
        return self.due_date < dt.datetime.now(dt.timezone.utc)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['due_date']
        abstract = True


class Task(AbstractTask):
    stakeholders = models.ManyToManyField('Stakeholder', blank=True)

    def get_absolute_url(self):
        return reverse('tasks:task-detail', kwargs={'pk': self.pk})


class Person(models.Model):
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    department = models.ForeignKey('Department', null=True, blank=False, on_delete=models.SET_NULL)

    def name(self):
        return f'{self.first} {self.last}'

    def __str__(self):
        return self.name()

    def get_absolute_url(self):
        return reverse('tasks:person-detail', kwargs={'pk': self.pk})


class Owner(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def name(self):
        return f'{self.person.first} {self.person.last}'

    def __str__(self):
        return self.name()

    def get_absolute_url(self):
        return reverse('tasks:owner-detail', kwargs={'pk': self.pk})


class Department(models.Model):
    name = models.CharField(max_length=100, help_text='Team or Department')

    def __str__(self):
        return self.name


class Stakeholder(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def name(self):
        return f'{self.person.first} {self.person.last}'

    def __str__(self):
        return self.name()


class SubTask(AbstractTask):
    owner = models.ForeignKey(Owner, null=True, blank=True, on_delete=models.SET_NULL)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('tasks:subtask-detail', kwargs={'pk': self.pk})
