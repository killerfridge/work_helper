# Generated by Django 2.2.4 on 2019-08-06 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_subtask_worktime'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subtask',
            old_name='worktime',
            new_name='work_time',
        ),
    ]