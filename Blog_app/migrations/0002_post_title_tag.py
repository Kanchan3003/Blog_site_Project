# Generated by Django 4.2.7 on 2023-11-19 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='DailyBlog!!', max_length=255),
        ),
    ]
