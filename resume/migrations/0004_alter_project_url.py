# Generated by Django 4.1.4 on 2022-12-18 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_remove_commonimage_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
