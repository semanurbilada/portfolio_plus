# Generated by Django 4.2.11 on 2024-05-17 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_about_alter_experience_end_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='about',
            name='updated_date',
        ),
        migrations.AlterField(
            model_name='about',
            name='about_button',
            field=models.CharField(blank=True, default='', max_length=254, verbose_name='About Button'),
        ),
    ]
