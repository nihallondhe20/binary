# Generated by Django 3.2.8 on 2023-08-13 02:58

from django.db import migrations, models
import service.models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0009_alter_user_request_raised'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='request_solve',
            field=models.DateField(default=service.models.default_next_5th_date),
        ),
    ]