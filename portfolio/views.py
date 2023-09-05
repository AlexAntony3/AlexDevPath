from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from .models import Home, About, Skill, Project, Education, Experience, Contact
from django.contrib.admin.views.decorators import staff_member_required


def HomePage(request):
    return render(request, 'pages/home.html')


def ShowAll(request):
    home = Home.objects.all()
    about = About.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    contact = Contact.objects.all()
    projects = Project.objects.all()
    skills = Skill.objects.all()
    context = {
        'home': home,
        'about': about,
        'education': education,
        'experience': experience,
        'contact': contact,
        'projects': projects,
        'skills': skills
        }

    if request.path == '/user/':
        return render(request, 'pages/user.html', context)
    else:
        return render(request, 'pages/home.html', context)


@staff_member_required
def user_view(request):
    return render(request, 'pages/user.html')


@staff_member_required
def dashboard_view(request):
    return render(request, 'pages/dashboard.html')
