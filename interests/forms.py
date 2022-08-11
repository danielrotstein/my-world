# Forms
from django import forms


# Models
from interests.models import Interest


class InterestCreateForm(forms.ModelForm):
    class Meta:
        model = Interest
        fields = [
            "name",
            "description",
            "image",
        ]