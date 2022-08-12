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


# --------- Movie Detail View ------------------------

def movie_detail_view(request, pk):
    movies_detail = Movie.objects.get(pk=pk)
    context = {
        "movies_detail": movies_detail
    }

    return render(request, "interests/movies/detail.html", context)
