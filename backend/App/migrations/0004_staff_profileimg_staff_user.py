# Generated by Django 4.2.2 on 2023-07-11 19:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App', '0003_rename_user_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='profileimg',
            field=models.ImageField(
                default='david-clode-oJlt2XBWuWs-unsplash.jpg', upload_to='profile_images'),
        ),
        migrations.AddField(
            model_name='staff',
            name='user',
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
