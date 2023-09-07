from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from .models import Home, About, Skill, Project, Education, Experience, Contact
from .forms import (AboutForm,
                    ProjectForm,
                    SkillForm,
                    ExperienceForm,
                    EducationForm
                    )


def show_all(request):
    """
    Handles all the request from all models
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
    """
    Initial view for the restricted admin/staff access
    """
    return render(request, 'pages/user.html')


@staff_member_required
def dashboard_view(request):
    """
    Dashboard view for the for admin/staff to access restricted CRUD material
    """
    projects = Project.objects.all()
    skills = Skill.objects.all()
    about = About.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    return render(request, 'pages/dashboard.html', {'projects': projects,
                                                    'skills': skills,
                                                    'about': about,
                                                    #'education': edcuation,
                                                    #'experience': experience
                                                    })


@staff_member_required
def create_project(request):
    """
    Functionality for unrestricted users to create projects
    """
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Project created Successfully!")
            return redirect('dashboard')

    context = {'form': form}
    return render(request, 'pages/project-form.html', context)


@staff_member_required
def create_skill(request):
    """
    Functionality for unrestricted users to create skills
    """
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Skill created Successfully!")
            return redirect('dashboard')

    context = {'form': form}
    return render(request, 'pages/skill-form.html', context)


@staff_member_required
def edit_project(request, pk):
    """
    Functionality for unrestricted users to edit projects
    """
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, "Project Edited Successfully!")
            return redirect('dashboard')

    context = {'form': form}
    return render(request, 'pages/project-form.html', context)


@staff_member_required
def edit_skill(request, pk):
    """
    Functionality for unrestricted users to edit skills
    """
    skill = Skill.objects.get(id=pk)
    form = SkillForm(instance=skill)

    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, "Skill Edited Successfully!")
            return redirect('dashboard')

    context = {'form': form}
    return render(request, 'pages/skill-form.html', context)


@staff_member_required
def delete_project(request, pk):
    """
    Functionality for unrestricted users to delete projects
    """
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, "Project Deleted Successfully!")
        return redirect('dashboard')

    context = {'project': project}
    return render(request, 'pages/delete-project.html', context)


@staff_member_required
def delete_skill(request, pk):
    """
    Functionality for unrestricted users to delete skils
    """
    skill = Skill.objects.get(id=pk)
    if request.method == 'POST':
        skill.delete()
        messages.success(request, "Skill Deleted Successfully!")
        return redirect('dashboard')

    context = {'skill': skill}
    return render(request, 'pages/delete-skill.html', context)
