# Generated by Django 4.2 on 2023-04-22 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='tasks',
            new_name='task',
        ),
    ]
