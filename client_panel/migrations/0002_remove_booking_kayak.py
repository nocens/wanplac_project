# Generated by Django 3.0.2 on 2020-02-27 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client_panel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='kayak',
        ),
    ]
