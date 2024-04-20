from django.shortcuts import render

# Create your views here.

# View as function: (but use views as Class)
def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')