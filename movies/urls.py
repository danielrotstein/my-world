from django.urls import path


# Models
from movies.views import (
    movie_list_view,
    movie_detail_view,
)


urlpatterns = [
    path("interests/movies/", movie_list_view, name="movies_list"),
    path("interests/movies/<int:pk>/", movie_detail_view,
         name="movies_detail"),
]
