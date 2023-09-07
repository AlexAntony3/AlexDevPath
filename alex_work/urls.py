"""alex_work URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from portfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_all, name="home"),
    path('user/', views.user_view, name="user"),
    path('user/dashboard/', views.dashboard_view, name="dashboard"),
    path('create-project/', views.create_project, name="create-project"),
    path('edit-project/<str:pk>/', views.edit_project, name="edit-project"),
    path('delete-project/<str:pk>/', views.delete_project, name="delete-project"),
    path('create-skill/', views.create_skill, name="create-skill"),
    path('edit-skill/<str:pk>/', views.edit_skill, name="edit-skill"),
    path('delete-skill/<str:pk>/', views.delete_skill, name="delete-skill"),
    path('edit-about/<str:pk>/', views.edit_about, name="edit-about"),
]
