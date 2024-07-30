# Generated by Django 5.0.6 on 2024-07-30 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.IntegerField(choices=[(1, 'Pending'), (2, 'Done')], default=1),
        ),
    ]