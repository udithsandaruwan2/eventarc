# Generated by Django 5.0.6 on 2024-07-10 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thoughts', '0002_rename_owner_thought_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thought',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]