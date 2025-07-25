# Generated by Django 5.2.4 on 2025-07-25 06:21

import django.db.models.deletion
import training.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('hours', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_code', models.CharField(default='', max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('certificate', models.FileField(blank=True, null=True, upload_to='certificates/')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='employee_photos/')),
                ('skills', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TrainingRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate', models.FileField(blank=True, null=True, upload_to='certificates/')),
                ('passed', models.BooleanField(default=False)),
                ('date', models.DateField(default=training.models.today_date)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training.course')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trainings', to='training.employee')),
            ],
        ),
    ]
