# Generated by Django 4.0.1 on 2022-06-04 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0025_historytask_delete_dailymotivation_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='register_date',
        ),
        migrations.AddField(
            model_name='user',
            name='weekly_task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='API.weeklyprogram'),
        ),
    ]
