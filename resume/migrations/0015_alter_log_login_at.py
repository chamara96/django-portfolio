# Generated by Django 4.1.4 on 2022-12-24 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0014_log_login_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='login_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
