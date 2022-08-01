from django.shortcuts import render, redirect


# UserCreationForm - creates a User (incl. username, password)
from django.contrib.auth.forms import UserCreationForm


# Login
from django.contrib.auth import login


# Create your views here.


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                print("Username or Password incorrect")

    form = UserCreationForm()
    context = {"form": form}

    return render(request, "registration/signup.html", context)
