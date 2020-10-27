# Generated by Django 3.1.2 on 2020-10-25 04:19

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('email_sender', '0007_auto_20201025_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='action',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='history',
            name='page',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='history',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 25, 9, 49, 1, 953630)),
        ),
        migrations.AlterField(
            model_name='history',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]