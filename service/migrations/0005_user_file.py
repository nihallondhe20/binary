# Generated by Django 3.2.8 on 2023-08-12 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_auto_20230812_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='file',
            field=models.FileField(null=True, upload_to='uploads/'),
        ),
    ]