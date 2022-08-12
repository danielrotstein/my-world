from django.shortcuts import render, redirect


# Models
from movies.models import Movie


# Forms
from movies.forms import (
    MovieCreateForm,
    MovieUpdateForm,
)

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


# --------- Movie Create View ------------------------

def movie_create_view(request):
    if request.method == "POST":
        form = MovieCreateForm(request.POST)
        if form.is_valid():
            create = form.save(commit=False)
            create.save()
            return redirect("movies_detail", create.pk)

    else:
        form = MovieCreateForm()

    context = {
        "form": form
    }

    return render(request, "interests/movies/create.html", context)


# --------- Movie Update View ------------------------

def movie_update_view(request, pk):
    movie_update = Movie.objects.get(pk=pk)
    if request.method == "POST":
        form = MovieUpdateForm(request.POST, instance=movie_update)
        if form.is_valid():
            update = form.save(commit=False)
            update.save()
            return redirect("movies_detail", update.pk)

    else:
        form = MovieUpdateForm()
    
    context = {
        "form": form
    }

    return render(request, "interests/movies/update.html", context)

