# Generated by Django 2.2.4 on 2019-08-04 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subtask',
            name='stakeholders',
        ),
    ]