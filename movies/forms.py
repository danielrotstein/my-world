from django import forms


# Models
from movies.models import Movie


class MovieCreateForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = [
            "name",
            "image",
            "overview",
            "movie_info",
            "year",
            "genre",
            "director",
            "producer",
            "runtime",
            "my_review",
        ]


class MovieUpdateForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = [
            "name",
            "image",
            "overview",
            "movie_info",
            "year",
            "genre",
            "director",
            "producer",
            "runtime",
            "my_review",
         ]