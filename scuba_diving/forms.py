# Forms
from django import forms


# Models
from scuba_diving.models import ScubaDiving


class ScubaCreateForm(forms.ModelForm):
    class Meta:
        model = ScubaDiving
        fields = [
            "location",
            "image",
            "description",
            "image6",
            "best_time",
            "languages",
            "currency",
            "timezone",
            "image2",
            "image3",
            "image4",
            "image5",
            "interest",
            ]


class ScubaUpdateForm(forms.ModelForm):
    class Meta:
        model = ScubaDiving
        fields = [
            "location",
            "image",
            "description",
            "image6",
            "best_time",
            "languages",
            "currency",
            "timezone",
            "image2",
            "image3",
            "image4",
            "image5",
            "interest",
        ]
