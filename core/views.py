from django.shortcuts import render
from core.models import GeneralSetting, ImageSetting, Experience

# Create your views here.
# View as function but use views as Classes!

def index(request):
    # General Settings: define variables
    site_title_setting = GeneralSetting.objects.get(name='site_title')
    site_keywords_setting = GeneralSetting.objects.get(name='site_keywords')
    about_preview_setting = GeneralSetting.objects.get(name='about_preview')

    # General Settings: parameters
    site_title = site_title_setting.parameters
    site_keywords = site_keywords_setting.parameters
    about_preview = about_preview_setting.parameters


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
    
    # Experiences: define variables
    # job_title_setting = Experience.objects.get(company_name='job_title')
    # company_name_setting = Experience.objects.get(company_name='company_name')
    # job_date_setting = Experience.objects.get(company_name='job_date')
    # job_description_setting = Experience.objects.get(company_name='job_description')
    # # Experiences: parameters
    # job_title = job_title_setting.company_name
    # company_name = company_name_setting.company_name
    # job_date = job_date_setting.company_name
    # job_description = job_description_setting.company_name

    context = {
        # general settings:
        'site_title': site_title, 
        'site_keywords': site_keywords, 
        'about_preview': about_preview, 

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
    }

    return render(request, 'index.html', context=context)

# def contact(request):
#     return render(request, 'contact.html')