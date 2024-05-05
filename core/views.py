from django.shortcuts import render
from core.models import GeneralSetting

# Create your views here.

# View as function: (but use views as Class)
def index(request):
    site_title_setting = GeneralSetting.objects.get(name='site_title')
    site_keywords_setting = GeneralSetting.objects.get(name='site_keywords')
    about_preview_setting = GeneralSetting.objects.get(name='about_preview')

    site_title = site_title_setting.parameters
    site_keywords = site_keywords_setting.parameters
    about_preview = about_preview_setting.parameters

    context = {
        'site_title': site_title, 
        'site_keywords': site_keywords, 
        'about_preview': about_preview, 
    }

    return render(request, 'index.html', context=context)

# def contact(request):
#     return render(request, 'contact.html')