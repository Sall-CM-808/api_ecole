# Generated by Django 5.2 on 2025-04-26 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matiere', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matiere',
            name='coefficient',
        ),
        migrations.AddField(
            model_name='matiere',
            name='poid_note_compos',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='matiere',
            name='poid_note_cours',
            field=models.IntegerField(default=1),
        ),
    ]
