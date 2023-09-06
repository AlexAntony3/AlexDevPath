from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from .models import Home, About, Skill, Project, Education, Experience, Contact
from .forms import AboutForm, ProjectForm, SkillForm, ExperienceForm, EducationForm


def show_all(request):
    """
    
    """
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
        'educations': education,
        'experiences': experience,
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
    projects = Project.objects.all()
    return render(request, 'pages/dashboard.html', {'projects': projects})


@staff_member_required
def create_project(request):

    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(form.errors)

    context = {'form': form}
    return render(request, 'pages/project-form.html', context)


@staff_member_required
def edit_project(request, pk):

    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    context = {'form': form}
    return render(request, 'pages/project-form.html', context)
