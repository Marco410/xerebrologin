# Generated by Django 3.1.5 on 2021-02-20 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_config_user_ncanales'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='config_user',
            name='user',
        ),
    ]