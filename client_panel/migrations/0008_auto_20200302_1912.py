# Generated by Django 3.0.2 on 2020-03-02 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client_panel', '0007_auto_20200302_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='term2',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='client_panel.Term'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='term',
            field=models.DateField(),
        ),
    ]