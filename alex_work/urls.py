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
    path('contact/', views.contact_me, name="contact"),
    path('dashboard/', views.dashboard_view, name="dashboard"),
    path('logout/', views.logout_view, name="logout"),
    path('create-project/', views.create_project, name="create-project"),
    path('edit-project/<str:pk>/', views.edit_project, name="edit-project"),
    path('delete-project/<str:pk>/', views.delete_project, name="delete-project"),
    path('create-skill/', views.create_skill, name="create-skill"),
    path('edit-skill/<str:pk>/', views.edit_skill, name="edit-skill"),
    path('delete-skill/<str:pk>/', views.delete_skill, name="delete-skill"),
    path('edit-about/<str:pk>/', views.edit_about, name="edit-about"),
    path('add-education/', views.add_education, name="add-education"),
    path('edit-education/<str:pk>/', views.edit_education, name="edit-education"),
    path('delete-education/<str:pk>/', views.delete_education, name="delete-education"),
    path('add-experience/', views.add_experience, name="add-experience"),
    path('edit-experience/<str:pk>/', views.edit_experience, name="edit-experience"),
    path('delete-experience/<str:pk>/', views.delete_experience, name="delete-experience"),
]
