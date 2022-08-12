from django.shortcuts import render


# Models
from movies.models import Movie

# Create your views here.


# --------- Movie List View ------------------------

def movie_list_view(request):
    movies_list = Movie.objects.all()
    context = {
        "movies_list": movies_list
        }

    return render(request, "interests/movies/list.html", context)
