from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    About_section1s = About_section1.objects.all()
    About_section2s = About_section2.objects.all()
    menu_list = menu.objects.all()
    context = {
        "About_section1s": About_section1s,
        "About_section2s": About_section2s,
        'menu_list': menu_list,
    } 
    return render(request, 'index.html', context)