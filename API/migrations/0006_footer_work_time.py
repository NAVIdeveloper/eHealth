# Generated by Django 4.0.1 on 2022-06-04 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0005_searchstatic'),
    ]

    operations = [
        migrations.AddField(
            model_name='footer',
            name='work_time',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]