# Generated by Django 3.2.8 on 2023-08-13 03:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0011_user_idss'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='idss',
        ),
    ]