# Generated by Django 3.0.5 on 2020-04-07 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client_panel', '0077_auto_20200407_0827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='exact_time',
        ),
        migrations.RemoveField(
            model_name='termkayaks',
            name='exact_time',
        ),
    ]