# Generated by Django 4.2.2 on 2023-07-24 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0011_alter_assets_asset_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='asset_image',
            field=models.ImageField(default='default.jpeg', upload_to='asset_images'),
        ),
    ]
