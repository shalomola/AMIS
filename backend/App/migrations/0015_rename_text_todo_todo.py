# Generated by Django 4.2.2 on 2023-07-24 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0014_todo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='text',
            new_name='todo',
        ),
    ]