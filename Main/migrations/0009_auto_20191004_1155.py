# Generated by Django 2.2.5 on 2019-10-04 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0008_auto_20191004_1150'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Bio',
            new_name='bio',
        ),
    ]
