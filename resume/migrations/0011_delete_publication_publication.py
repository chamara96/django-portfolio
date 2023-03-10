# Generated by Django 4.1.4 on 2022-12-22 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0010_remove_certificate_logo_certificate_logo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Publication',
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('title', models.CharField(max_length=255, null=True)),
                ('institute', models.CharField(max_length=255, null=True)),
                ('date', models.DateField(null=True)),
                ('url', models.CharField(max_length=255, null=True)),
                ('logo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='resume.commonimage')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
