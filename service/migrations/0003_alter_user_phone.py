# Generated by Django 3.2.8 on 2023-08-12 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20230812_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.BigIntegerField(max_length=10),
        ),
    ]