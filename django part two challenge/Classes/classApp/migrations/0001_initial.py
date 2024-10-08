# Generated by Django 5.1.1 on 2024-09-25 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='djangoClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('course_number', models.IntegerField()),
                ('instructor_name', models.CharField(max_length=60)),
                ('duration', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'Django Classes',
            },
        ),
    ]
