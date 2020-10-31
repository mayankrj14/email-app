# Generated by Django 3.1.2 on 2020-10-25 03:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_sender', '0004_auto_20201025_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='email_from',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='history',
            name='email_to',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='history',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 25, 9, 11, 50, 110034)),
        ),
    ]