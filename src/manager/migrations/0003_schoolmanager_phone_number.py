# Generated by Django 5.2 on 2025-04-24 09:22

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolmanager',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default=0, max_length=128, region=None, unique=True),
        ),
    ]
