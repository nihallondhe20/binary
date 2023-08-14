# Generated by Django 3.2.8 on 2023-08-13 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_user_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('R', 'REQUEST_RCV'), ('A', 'REQ_ASSIGN'), ('P', 'PENDING'), ('S', 'SOLVE')], default='R', max_length=255),
        ),
    ]
