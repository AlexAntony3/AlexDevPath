from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from .models import Home, About, Skill, Project, Education, Experience, Contact


def redirect_if_not_admin(fn):
    def wrapper(request):
        if request.user.is_superuser:
            return fn(request)
        else:
            return HttpResponseRedirect('/')
    return wrapper


def HomePage(request):
    return render(request, 'pages/home.html')


def ShowAll(request):
    home = Home.objects.all()
    about = About.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    contact = Contact.objects.all()
    projects = Project.objects.all()
    context = {
        'home': home,
        'about': about,
        'education': education,
        'experience': experience,
        'contact': contact,
        'projects': projects
        }

    return render(request, 'pages/home.html', context)


def SkillSection(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()
    context = {
        'projects': projects, 'skills': skills
    }

    return render(request, 'pages/skill.html', context)


@redirect_if_not_admin
def dashboard_view(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()
    context = {
        'projects': projects, 'skills': skills
    }

    return render(request, 'pages/dashboard.html', context)
