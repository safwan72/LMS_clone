# Generated by Django 3.1.7 on 2021-03-15 18:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Work2', '0006_quiz_quiz_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='gradedquiz',
            name='quiz_graded',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 3, 15, 18, 26, 51, 472932)),
            preserve_default=False,
        ),
    ]
