from .models import About, Project, Skill, Experience, Education
from django import forms


class AboutForm(forms.ModelForm):
    """
    
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
    Get custom menu item name labels for checkboxes
    """
    def label_from_instance(self, skills):
        """
        Returns labels
        """
        return str(skills)


class ProjectForm(forms.ModelForm):
    """

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
    
    """
    class Meta:
        model = Skill
        fields = ['name',
                  'proficiency',
                  'icon',]


class ExperienceForm(forms.ModelForm):
    """
    
    """
    class Meta:
        model = Experience
        fields = ['company',
                  'start_date',
                  'description']


class EducationForm(forms.ModelForm):
    """
    
    """
    class Meta:
        model = Education
        fields = ['qualification',
                  'start_date',
                  'description']
