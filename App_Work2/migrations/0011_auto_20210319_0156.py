# Generated by Django 3.1.7 on 2021-03-19 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0001_initial'),
        ('App_Work2', '0010_auto_20210319_0140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gradedquiz',
            name='taken_by',
        ),
        migrations.CreateModel(
            name='StudentQuiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_quiz_view', to='App_Work2.quiz')),
                ('taker', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_quiz', to='App_Login.student')),
            ],
        ),
        migrations.AlterField(
            model_name='gradedquiz',
            name='quiz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_graded_quiz', to='App_Work2.studentquiz'),
        ),
    ]
