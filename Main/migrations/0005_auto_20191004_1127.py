# Generated by Django 2.2.5 on 2019-10-04 11:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0004_auto_20191004_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthday',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
    ]
