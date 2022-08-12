from django.urls import path


# Models
from movies.views import movie_list_view


urlpatterns = [
    path("interests/movies/", movie_list_view, name="movies_list"),
]
