# Generated by Django 5.0.4 on 2024-05-21 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_todo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Todo',
        ),
    ]
