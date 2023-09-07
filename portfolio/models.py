from django.db import models
from django.contrib import admin
from cloudinary.models import CloudinaryField


class Home(models.Model):
    """
    Defines the fields required in the home model.
    """
    title = models.CharField(max_length=200, blank=True)
    main_image = CloudinaryField('image')
    name_header = models.CharField(max_length=100)
    intro_description = models.TextField()

    def __str__(self):
        """
        returns a string response with the title for the admin
        """
        return self.title


class About(models.Model):
    """
    Defines the about model with numerous fields
    """
    title = models.CharField(max_length=50, blank=True)
    second_image = CloudinaryField('image')
    first_name = models.CharField(max_length=80, unique=True)
    last_name = models.CharField(max_length=80, unique=True)
    age = models.IntegerField(null=True, blank=True)
    nationality = models.CharField(max_length=200)
    languages = models.CharField(max_length=200)
    address = models.CharField(max_length=400, unique=True)

    def __str__(self):
        """
        returns a string response with the title 
        in the about section for the admin
        """
        return self.title


class Project(models.Model):
    """
    defines the project model which will exhibit
    all projects and skills utilised.
    """
    name = models.CharField(max_length=100, unique=True)
    thumbnail = CloudinaryField('image')
    skills = models.ManyToManyField('Skill')
    description = models.TextField()
    live_url = models.URLField()
    github_URL = models.URLField()

    def __str__(self):
        """
        returns a string response with the name of the project to the admin
        """
        return self.name


class Skill(models.Model):
    """
    defines the skill model which will exhibit proficiency in the skill
    """
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField()
    icon = models.CharField(max_length=100)

    def __str__(self):
        """
        returns a string response with the name of the skill to the admin
        """
        return self.name


class Experience(models.Model):
    """
    defines the experience model from which the work history can be presented
    """
    role = models.CharField(max_length=200)
    company = models.CharField(max_length=300)
    start_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        """
        returns a string response with the role and company to the admin
        """
        return f'{self.role} at {self.company}'


class Education(models.Model):
    """
    defines the education model from which 
    the education history can be presented
    """
    institute = models.CharField(max_length=200)
    qualification = models.CharField(max_length=200)
    start_date = models.DateField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        """
        returns a string response with the qualification
        and insitute to the admin
        """
        return f'{self.qualification} from {self.institute}'


class Contact(models.Model):
    """
    defines the contact model in which a user can make contact with the admin
    """
    full_name = models.CharField(max_length=200)
    number = models.CharField(max_length=16)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        """
        returns a string with a brief summary of the sender name and message
        """
        return f'{self.full_name} sent a message stating {self.message}'
