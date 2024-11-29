# Generated by Django 5.1.3 on 2024-11-29 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='tag',
        ),
        migrations.AddField(
            model_name='question',
            name='tag',
            field=models.ManyToManyField(related_name='questions', to='posts.tag'),
        ),
    ]