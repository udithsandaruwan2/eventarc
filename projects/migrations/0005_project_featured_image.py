# Generated by Django 5.0.4 on 2024-05-03 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, default='logo.png', null=True, upload_to=''),
        ),
    ]
