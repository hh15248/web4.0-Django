# Generated by Django 4.0.3 on 2022-04-12 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0010_friend_best_school'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='best_school',
        ),
    ]