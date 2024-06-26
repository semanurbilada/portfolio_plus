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


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['id', 'about_title', 'about_title_colored', 'about_content_1', 'about_content_2', 'about_button']
    search_fields = ['id', 'about_title', 'about_title_colored']
    list_editable = ['about_title', 'about_title_colored', 'about_content_1', 'about_content_2', 'about_button']

    class Meta:
        model = About

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'project_title', 'project_category', 'project_link', 'project_description', 'data_groups']
    search_fields = ['id', 'project_title', 'project_category']
    list_editable = ['project_title', 'project_category', 'project_link', 'project_description', 'data_groups']

    class Meta:
        model = Project


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'slug', 'button_text', 'file']
    search_fields =['id', 'slug', 'button_text']
    list_editable = ['order', 'slug', 'button_text', 'file']

    class Meta:
        model = Document
