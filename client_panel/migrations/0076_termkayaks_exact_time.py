# Generated by Django 3.0.2 on 2020-04-03 11:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('client_panel', '0075_auto_20200401_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='termkayaks',
            name='exact_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
