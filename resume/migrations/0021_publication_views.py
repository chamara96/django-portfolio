# Generated by Django 4.1.4 on 2023-01-09 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0020_alter_demo_icon_alter_socialmedia_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='views',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
