# Generated by Django 3.0.2 on 2020-03-20 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client_panel', '0058_auto_20200320_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='client_panel.DateList'),
        ),
    ]
