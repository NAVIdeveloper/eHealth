# Generated by Django 4.0.1 on 2022-06-13 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0005_weeklyprogram_last_update'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weeklyprogram',
            name='last_update',
        ),
    ]
