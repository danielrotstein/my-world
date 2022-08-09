from django.shortcuts import render


from intro.models import Intro


# Create your views here.


def intro_list_view(request):
    intro_list = Intro.objects.all()
    context = {"intro_list": intro_list}

    return render(request, "intro/list.html", context)
