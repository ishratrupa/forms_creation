from django.shortcuts import render,redirect
from .forms import *
from django.contrib import


from .models import *

# Create your views here.

def index(requests):
    profile =Profile.objects.all()
    context = {
        'profile':profile
    }
    return render(requests, 'new_app/index.html',context)

def contact(requests):
    return render(requests, 'new_app/contact.html')

def  projects(requests):
    return render(requests, 'new_app/projects.html')

def resume(requests):
    return render(requests, 'new_app/resume.html')





