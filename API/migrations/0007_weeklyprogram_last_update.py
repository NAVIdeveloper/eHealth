# Generated by Django 4.0.1 on 2022-06-13 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0006_remove_weeklyprogram_last_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='weeklyprogram',
            name='last_update',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]