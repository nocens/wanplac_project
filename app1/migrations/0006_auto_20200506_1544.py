# Generated by Django 3.0.5 on 2020-05-06 13:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20200506_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='phone',
            field=models.CharField(max_length=13, validators=[django.core.validators.RegexValidator('^[0-9]*$', message='Numer telefonu może zawierać tylko cyfry.')]),
        ),
    ]
