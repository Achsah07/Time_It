# Generated by Django 5.1.2 on 2024-11-02 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable_generator', '0004_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem_name', models.CharField(max_length=40)),
            ],
        ),
    ]
