# Generated by Django 4.2.7 on 2023-11-09 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.IntegerField(choices=[(1, 'usuário moderador'), (2, 'usuário master'), (3, 'usuário normal')], default=3),
        ),
    ]
