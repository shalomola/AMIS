# Generated by Django 4.2.2 on 2023-07-26 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0015_rename_text_todo_todo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Positions',
        ),
        migrations.RemoveField(
            model_name='assetsissuance',
            name='asset_location',
        ),
        migrations.AlterField(
            model_name='assetsissuance',
            name='asset_assignee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.staff'),
        ),
    ]