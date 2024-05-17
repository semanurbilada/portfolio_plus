# Generated by Django 4.2.11 on 2024-05-17 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_experience_end_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('about_title', models.CharField(blank=True, default='', max_length=254, verbose_name='About Title')),
                ('about_title_colored', models.CharField(blank=True, default='', max_length=254, verbose_name='About Title Colored')),
                ('about_content', models.CharField(blank=True, default='', max_length=254, verbose_name='About Content')),
                ('about_button', models.CharField(blank=True, default='', max_length=254, verbose_name='About Content')),
            ],
            options={
                'verbose_name': 'About',
            },
        ),
        migrations.AlterField(
            model_name='experience',
            name='end_date',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='End Date'),
        ),
    ]
