# Generated by Django 2.0.6 on 2018-06-17 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_entry', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='id_num',
        ),
        migrations.RemoveField(
            model_name='data',
            name='num',
        ),
        migrations.RemoveField(
            model_name='data',
            name='text',
        ),
    ]
