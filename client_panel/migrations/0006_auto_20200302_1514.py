# Generated by Django 3.0.2 on 2020-03-02 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client_panel', '0005_auto_20200229_1406'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kayak',
            old_name='quantity',
            new_name='store',
        ),
    ]
