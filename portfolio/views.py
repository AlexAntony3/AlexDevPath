from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required


def HomePage(request):
    return render(request, 'pages/home.html')


def ProjectPage(request, id):
    context = {'id': id}
    return render(request, 'pages/project.html', context)


@login_required(login_url='admin:login')
def Dashboard(request):
    return render(request, 'pages/dashboard.html')

