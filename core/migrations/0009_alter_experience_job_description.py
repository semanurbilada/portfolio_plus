# Generated by Django 4.2.11 on 2024-05-12 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_experience_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='job_description',
            field=models.CharField(blank=True, default='', max_length=750, verbose_name='Job Description'),
        ),
    ]