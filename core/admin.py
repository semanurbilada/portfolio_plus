from django.contrib import admin
from core.models import *

# Register your models here.

@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'parameters', 'updated_date', 'created_date']
    search_fields = ['id', 'name', 'description', 'parameters']
    list_editable = ['description', 'parameters']

    class Meta:
        models = GeneralSetting


@admin.register(ImageSetting)
class ImageSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'file', 'updated_date', 'created_date']
    search_fields = ['id', 'name', 'description', 'file']
    list_editable = ['description', 'file']

    class Meta:
        models = ImageSetting


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_name', 'job_title', 'job_description', 'job_period', 'start_date', 'end_date']
    search_fields = ['id', 'company_name', 'job_title']
    list_editable = ['company_name', 'job_title', 'job_description', 'job_period', 'start_date', 'end_date']

    class Meta:
        models = Experience