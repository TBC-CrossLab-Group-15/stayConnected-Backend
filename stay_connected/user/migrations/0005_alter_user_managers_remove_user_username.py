# Generated by Django 5.1.3 on 2024-12-01 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_user_correct_answers_user_my_answers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]