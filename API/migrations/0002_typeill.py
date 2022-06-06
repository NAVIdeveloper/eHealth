# Generated by Django 4.0.1 on 2022-06-04 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeIll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(max_length=255)),
                ('title_ru', models.CharField(max_length=255)),
                ('title_en', models.CharField(max_length=255)),
                ('text1_uz', models.TextField()),
                ('text1_ru', models.TextField()),
                ('text1_en', models.TextField()),
                ('text2_uz', models.TextField()),
                ('text2_ru', models.TextField()),
                ('text2_en', models.TextField()),
                ('text3_uz', models.TextField()),
                ('text3_ru', models.TextField()),
                ('text3_en', models.TextField()),
                ('text4_uz', models.TextField()),
                ('text4_ru', models.TextField()),
                ('text4_en', models.TextField()),
                ('text5_uz', models.TextField()),
                ('text5_ru', models.TextField()),
                ('text5_en', models.TextField()),
                ('img', models.ImageField(upload_to='ill/')),
            ],
        ),
    ]