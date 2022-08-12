from django.urls import path


# Models
from movies.views import (
    movie_list_view,
    movie_detail_view,
    movie_create_view,
    movie_update_view,
)


urlpatterns = [
    path("interests/movies/", movie_list_view, name="movies_list"),
    path("interests/movies/<int:pk>/", movie_detail_view,
         name="movies_detail"),
    path("interests/movies/create/", movie_create_view,
         name="movies_create"),
    path("interests/movies/<int:pk>/update/", movie_update_view,
         name="movies_update"),
]
