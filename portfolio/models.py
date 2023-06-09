from django.db import models
from django.contrib import admin
from cloudinary.models import CloudinaryField


class Home(models.Model):
    title = models.CharField(max_length=200, blank=True)
    main_image = CloudinaryField('image')
    name_header = models.CharField(max_length=100)
    intro_description = models.TextField()

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=50, blank=True)
    second_image = CloudinaryField('image')
    first_name = models.CharField(max_length=80, unique=True)
    last_name = models.CharField(max_length=80, unique=True)
    age = models.IntegerField(null=True, blank=True)
    nationality = models.CharField(max_length=200)
    languages = models.CharField(max_length=200)
    address = models.CharField(max_length=400, unique=True)
    freelance = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Project(models.Model):
    name = models.CharField(max_length=100, unique=True)
    thumbnail = CloudinaryField('image')
    skills = models.ManyToManyField('Skill')
    description = models.TextField()
    live_url = models.URLField()
    github_URL = models.URLField()

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField()
    icon = CloudinaryField('image')

    def __str__(self):
        return self.name


class Experience(models.Model):
    role = models.CharField(max_length=200)
    company = models.CharField(max_length=300)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f'{self.role} at {self.company}'


class Education(models.Model):
    institute = models.CharField(max_length=200)
    qualification = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.qualification} from {self.institute}'


class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    number = models.CharField(max_length=16)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f'{self.full_name} sent a message stating {self.message}'
