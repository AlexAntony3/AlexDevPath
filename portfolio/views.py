from django.shortcuts import render
from django.views import generic


def HomePage(request):
    return render(request, 'index.html')
