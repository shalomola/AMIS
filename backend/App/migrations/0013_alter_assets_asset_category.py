# Generated by Django 4.2.2 on 2023-07-24 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0012_alter_assets_asset_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='asset_category',
            field=models.CharField(max_length=100),
        ),
    ]
