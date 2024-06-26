# Generated by Django 5.0.4 on 2024-05-04 06:15

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_featured_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='review_total',
            new_name='like_total',
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('body', models.TextField(blank=True, null=True)),
                ('value', models.CharField(choices=[('LIKE', 'LIKE VOTE'), ('UNLIKE', 'UNLIKE VOTE')], max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
