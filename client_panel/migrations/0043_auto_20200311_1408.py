# Generated by Django 3.0.2 on 2020-03-11 13:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_panel', '0042_datelist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.CharField(default=datetime.date(2020, 3, 12), max_length=32),
        ),
    ]