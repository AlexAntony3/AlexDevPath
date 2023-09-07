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
                  'address',
                  'freelance']


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


class ExperienceForm(forms.ModelForm):
    """
    Allows the user to have CRUD functionality of work history
    """
    class Meta:
        model = Experience
        fields = ['company',
                  'role',
                  'start_date',
                  'end_date',
                  'description']


class EducationForm(forms.ModelForm):
    """
    Allows the user to have CRUD functionality of education history
    """
    class Meta:
        model = Education
        fields = ['qualification',
                  'institute',
                  'start_date',
                  'end_date',
                  'description']
