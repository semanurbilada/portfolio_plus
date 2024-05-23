from django.shortcuts import render, redirect, get_object_or_404
from core.models import GeneralSetting, ImageSetting, Experience, About, Project, Document

# Create your views here.
# View as function but use views as Classes!

def index(request):
    # General Settings: define variables
    site_title_setting = GeneralSetting.objects.get(name='site_title')
    site_content_setting = GeneralSetting.objects.get(name='site_content')
    home_title_setting = GeneralSetting.objects.get(name='home_title')
    home_text_setting = GeneralSetting.objects.get(name='home_text')
    home_button_setting = GeneralSetting.objects.get(name='home_button')
    site_keywords_setting = GeneralSetting.objects.get(name='site_keywords')
    about_preview_setting = GeneralSetting.objects.get(name='about_preview')
    photos_title_setting = GeneralSetting.objects.get(name='photos_title')
    contact_title_setting = GeneralSetting.objects.get(name='contact_title')
    projects_title_setting = GeneralSetting.objects.get(name='projects_title')
    experience_title_setting = GeneralSetting.objects.get(name='experience_title')

    nav_link_1_setting = GeneralSetting.objects.get(name='nav_link_1')
    nav_link_2_setting = GeneralSetting.objects.get(name='nav_link_2')
    nav_link_3_setting = GeneralSetting.objects.get(name='nav_link_3')
    nav_link_4_setting = GeneralSetting.objects.get(name='nav_link_4')
    nav_link_5_setting = GeneralSetting.objects.get(name='nav_link_5')
    nav_link_6_setting = GeneralSetting.objects.get(name='nav_link_6')

    # General Settings: parameters
    site_title = site_title_setting.parameters
    site_content = site_content_setting.parameters
    home_title = home_title_setting.parameters
    home_text = home_text_setting.parameters
    home_button = home_button_setting.parameters
    site_keywords = site_keywords_setting.parameters
    about_preview = about_preview_setting.parameters
    photos_title = photos_title_setting.parameters
    contact_title = contact_title_setting.parameters
    projects_title = projects_title_setting.parameters
    experience_title = experience_title_setting.parameters

    nav_link_1 = nav_link_1_setting.parameters
    nav_link_2 = nav_link_2_setting.parameters
    nav_link_3 = nav_link_3_setting.parameters
    nav_link_4 = nav_link_4_setting.parameters
    nav_link_5 = nav_link_5_setting.parameters
    nav_link_6 = nav_link_6_setting.parameters


    # Image Settings: define variables
    home_bg_setting = ImageSetting.objects.get(name='home_bg')
    home_shape_setting = ImageSetting.objects.get(name='home_shape')
    home_profile_setting = ImageSetting.objects.get(name='home_profile')

    photo1_setting = ImageSetting.objects.get(name='photo1')
    photo2_setting = ImageSetting.objects.get(name='photo2')
    photo3_setting = ImageSetting.objects.get(name='photo3')
    photo4_setting = ImageSetting.objects.get(name='photo4')
    photo5_setting = ImageSetting.objects.get(name='photo5')
    photo6_setting = ImageSetting.objects.get(name='photo6')
    photo7_setting = ImageSetting.objects.get(name='photo7')
    photo8_setting = ImageSetting.objects.get(name='photo8')

    about_setting = ImageSetting.objects.get(name='about')
    overlay_setting = ImageSetting.objects.get(name='overlay')
    site_favicon_setting = ImageSetting.objects.get(name='site_favicon')
    header_logo_setting = ImageSetting.objects.get(name='header_logo')
    header_logo_light_setting = ImageSetting.objects.get(name='header_logo_light')

    # Image Settings: parameters
    home_bg = home_bg_setting.file
    home_shape = home_shape_setting.file
    home_profile = home_profile_setting.file

    photo1 = photo1_setting.file
    photo2 = photo2_setting.file
    photo3 = photo3_setting.file
    photo4 = photo4_setting.file
    photo5 = photo5_setting.file
    photo6 = photo6_setting.file
    photo7 = photo7_setting.file
    photo8 = photo8_setting.file

    about = about_setting.file
    overlay = overlay_setting.file
    site_favicon = site_favicon_setting.file
    header_logo = header_logo_setting.file
    header_logo_light = header_logo_light_setting.file

    # Experience:
    experiences = Experience.objects.all()

    # About:
    about_sections = About.objects.all()

    # Document:
    document = Document.objects.first()

    # Projects:
    projects = Project.objects.all()
    # extract categories and data groups from projects
    categories = {(project.project_category, project.data_groups) for project in projects}

    context = {
        # general settings:
        'site_title': site_title, 
        'site_content': site_content, 
        'home_title': home_title,
        'home_text': home_text,
        'home_button': home_button,
        'site_keywords': site_keywords, 
        'about_preview': about_preview, 
        'photos_title': photos_title,
        'projects_title': projects_title,
        'contact_title': contact_title,
        'experience_title': experience_title,
        
        'nav_link_1': nav_link_1,
        'nav_link_2': nav_link_2,
        'nav_link_3': nav_link_3,
        'nav_link_4': nav_link_4,
        'nav_link_5': nav_link_5,
        'nav_link_6': nav_link_6,

        # images settings:
        'home_bg': home_bg,
        'home_shape': home_shape,
        'home_profile': home_profile,

        'photo1': photo1,
        'photo2': photo2,
        'photo3': photo3,
        'photo4': photo4,
        'photo5': photo5,
        'photo6': photo6,
        'photo7': photo7,
        'photo8': photo8,

        'about': about,
        'overlay': overlay,
        'site_favicon': site_favicon,
        'header_logo': header_logo,
        'header_logo_light': header_logo_light,

        #experiences:
        'experiences': experiences,

        #about:
        'about_sections': about_sections,

        #projects:
        'projects': projects,
        'categories': categories,

        #documents:
        'document': document,
    }

    return render(request, 'index.html', context=context)


def redirect_urls(slug):
    document = get_object_or_404(Document, slug=slug)
    return redirect(document.file.url)