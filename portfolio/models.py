from django.db import models
from cloudinary.models import CloudinaryField


class Home(models.Model):
    title = models.CharField(max_length=200, blank=True)
    main_image = models.CloudinaryField('image')
    name_header = models.CharField(max_length=100)
    intro_description = models.TextField()


