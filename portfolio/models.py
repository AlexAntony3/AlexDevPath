from django.db import models
from cloudinary.models import CloudinaryField


class Home(models.Model):
    title = models.CharField(max_length=200, blank=True)
    main_image = models.CloudinaryField('image')
    name_header = models.CharField(max_length=100)
    intro_description = models.TextField()


class About(models.Model):
    title = models.CharField(max_length=50, blank=True)
    second_image = models.CloudinaryField('image')
    first_name = CharField(max_length=80, unique=True)
    last_name = CharField(max_length=80, unique=True)
    age = models.IntegerField(null=True, blank=True)
    nationality = models.CharField(max_length=200)
    languages = models.CharField(max_length=200)
    address = models.CharField(max_length=400, unique=True)
    freelance = models.BooleanField(default=False)
