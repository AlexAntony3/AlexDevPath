from .models import About, Project, Skill, Experience, Education
from django import forms


class AboutForm(forms.ModelForm):
    """
    Interaction required for the user to update/enter 'about me' details
    """
    class Meta:
        model = About
        fields = ['second_image',
                  'age',
                  'nationality',
                  'languages',
                  'address']

        widgets = {
            "second_image": forms.FileInput(attrs={"class": "form-control form-style"}),
            "age": forms.NumberInput(attrs={"class": "form-control form-style", "placeholder": "Type in your age"}),
            "nationality": forms.TextInput(attrs={"class": "form-control form-style", "placeholder": "Enter your nationality"}),
            "languages": forms.TextInput(attrs={"class": "form-control form-style", "placeholder": "What languages do you speak?"}),
            "address": forms.TextInput(attrs={"class": "form-control form-style", "placeholder": "Enter your city and country"}),
        }


class CustomMMCF(forms.ModelMultipleChoiceField):
    """
    Get unrestricted user entered skill name labels for checkboxes
    """
    def label_from_instance(self, skills):
        """
        Returns labels
        """
        return str(skills)


class ProjectForm(forms.ModelForm):
    """
    The required fields required for CRUD functionality for the project
    This also incorporates the CustomMMCF function to allow the user to
    pick more than one skill per project
    """
    class Meta:
        model = Project
        fields = ['name',
                  'thumbnail',
                  'skills',
                  'description',
                  'live_url',
                  'github_URL',]

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control form-style", "placeholder": "Enter in your Skill"}),
            "thumbnail": forms.FileInput(attrs={"class": "form-control form-style"}),
            "skills": forms.RadioSelect(attrs={"class": "form-control form-style", "placeholder": "Write a devicon friendly icon e.g. html5"}),
            "description": forms.Textarea(attrs={"rows": "3", "class": "form-control form-style", "placeholder": "Write a brief description of your role"}),
            "live_url": forms.URLInput(attrs={"class": "form-control form-style", "placeholder": "Enter your live url in https://... format"}),
            "github_URL": forms.URLInput(attrs={"class": "form-control form-style", "placeholder": "Enter your GitHub url in https://... format"})
        }

    skills = CustomMMCF(
            queryset=Skill.objects.all(),
            widget=forms.CheckboxSelectMultiple()
        )


class SkillForm(forms.ModelForm):
    """
    Allows the user to have CRUD functionality of skills
    """
    class Meta:
        model = Skill
        fields = ['name',
                  'proficiency',
                  'icon',]

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control form-style", "placeholder": "Enter in your Skill"}),
            "proficiency": forms.NumberInput(attrs={"class": "form-control form-style", "placeholder": "Enter a number between 0-100"}),
            "icon": forms.TextInput(attrs={"class": "form-control form-style", "placeholder": "Write a devicon friendly icon e.g. html5"}),
        }


class ExperienceForm(forms.ModelForm):
    """
    Allows the user to have CRUD functionality of work history
    """
    class Meta:
        model = Experience
        fields = ['company',
                  'role',
                  'start_date',
                  'description']

        widgets = {
            "company": forms.TextInput(attrs={"class": "form-control form-style", "placeholder": "Enter in your Company name"}),
            "role": forms.TextInput(attrs={"class": "form-control form-style", "placeholder": "Enter in your role"}),
            "start_date": forms.DateInput(attrs={"class": "form-control form-style", "placeholder": "Enter in your start date in the format YYYY-MM-DD"}),
            "description": forms.Textarea(attrs={"rows": "3", "class": "form-control form-style", "placeholder": "Write a brief description of your role"}),
        }


class EducationForm(forms.ModelForm):
    """
    Allows the user to have CRUD functionality of education history
    """
    class Meta:
        model = Education
        fields = ['qualification',
                  'institute',
                  'start_date',
                  'description']

        widgets = {
            "qualification": forms.TextInput(attrs={"class": "form-control form-style", "placeholder": "Enter in your qualification"}),
            "institute": forms.TextInput(attrs={"class": "form-control form-style", "placeholder": "Enter in your institute"}),
            "start_date": forms.DateInput(attrs={"class": "form-control form-style", "placeholder": "Enter in your start date in the format YYYY-MM-DD"}),
            "description": forms.Textarea(attrs={"rows": "3", "class": "form-control form-style", "placeholder": "Write a brief description of your education"}),
        }
