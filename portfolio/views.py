from django.shortcuts import render
from django.views import generic


def HomePage(request):
    return render(request, 'pages/home.html')


def ProjectPage(request, id):
    context = {'id': id}
    return render(request, 'pages/project.html', context)

