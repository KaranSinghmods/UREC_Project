# Generated by Django 4.1.2 on 2022-12-07 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urec_app', '0008_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_time_completion',
            field=models.DateTimeField(),
        ),
    ]