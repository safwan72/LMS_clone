# Generated by Django 3.1.7 on 2021-03-19 03:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_Work2', '0013_auto_20210319_0307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentquiz',
            name='quiz',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_quiz_view', to='App_Work2.quiz'),
        ),
    ]
