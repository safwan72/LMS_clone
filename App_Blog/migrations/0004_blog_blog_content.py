# Generated by Django 3.1.7 on 2021-03-16 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Blog', '0003_auto_20210316_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_content',
            field=models.TextField(blank=True),
        ),
    ]
