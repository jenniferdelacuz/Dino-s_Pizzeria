# Generated by Django 3.1 on 2021-09-28 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210927_1730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='STATUS',
        ),
    ]
