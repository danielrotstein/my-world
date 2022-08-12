# Forms
from django import forms


# Models
from scuba_diving.models import ScubaDiving


class ScubaCreateForm(forms.ModelForm):
    class Meta:
        model = ScubaDiving
        fields = [
            "location",
            "description",
            "image",
        ]


class ScubaUpdateForm(forms.ModelForm):
    class Meta:
        model = ScubaDiving
        fields = [
            "location",
            "description",
            "image",
        ]