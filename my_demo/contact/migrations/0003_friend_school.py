# Generated by Django 4.0.3 on 2022-04-11 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_rename_contact_friend'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='school',
            field=models.CharField(choices=[(1, 'I LOVE UT'), (0, 'I hate it (I got rejected)')], default='I LOVE UT', max_length=120),
        ),
    ]
