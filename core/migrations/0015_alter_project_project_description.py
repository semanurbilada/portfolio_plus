# Generated by Django 4.2.11 on 2024-05-18 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_description',
            field=models.TextField(max_length=255),
        ),
    ]