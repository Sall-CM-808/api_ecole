# Generated by Django 5.2 on 2025-04-24 11:06

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_rename_schoolmanager_schoolmanagers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolmanagers',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='000000000', max_length=128, region=None, unique=True),
        ),
    ]
