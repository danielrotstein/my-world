# Forms
from django import forms


# Models
from projects.models import Project


class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "name",
            "description",
            "members",
        ]
