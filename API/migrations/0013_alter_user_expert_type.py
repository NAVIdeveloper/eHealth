# Generated by Django 4.0.1 on 2022-05-23 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0012_user_expert_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='expert_type',
            field=models.IntegerField(blank=True, choices=[(1, 'dietolog'), (2, 'sportsmen')], null=True),
        ),
    ]
