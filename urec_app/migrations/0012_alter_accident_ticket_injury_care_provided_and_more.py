# Generated by Django 4.1.2 on 2022-12-07 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urec_app', '0011_alter_task_date_time_completion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accident_ticket_injury',
            name='care_provided',
            field=models.TextField(max_length=1023),
        ),
        migrations.AlterField(
            model_name='accident_ticket_injury',
            name='injury_description',
            field=models.TextField(max_length=1023),
        ),
    ]
